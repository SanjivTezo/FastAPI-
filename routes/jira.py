from fastapi import APIRouter, HTTPException
import httpx
import base64
import os
from dotenv import load_dotenv
router = APIRouter()

load_dotenv()
JIRA_URL = "https://tezo-team-zjtc62v2.atlassian.net/rest/api/3/project"
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not JIRA_USERNAME or not JIRA_API_TOKEN:
    raise Exception("JIRA_USERNAME and JIRA_API_TOKEN must be set in the environment variables.")

basic_auth = base64.b64encode(f"{JIRA_USERNAME}:{JIRA_API_TOKEN}".encode()).decode()


@router.get("/jira/projects")
async def get_jira_projects():
    headers = {
        "Authorization": f"Basic {basic_auth}",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(JIRA_URL, headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch Jira projects")

        project= response.json()
        simplified_projects = [
            {
                "id": project["id"],
                "key": project["key"],
                "name": project["name"],
                "projectTypeKey": project["projectTypeKey"],
                "isPrivate": project["isPrivate"]
            }
            for project in project
        ]
        return simplified_projects

    