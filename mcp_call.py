import asyncio
from copilot import CopilotClient
from copilot.session import PermissionHandler

async def main():
    client = CopilotClient()
    await client.start()

    session = await client.create_session(on_permission_request=PermissionHandler.approve_all, model="auto", mcp_servers={        
        # Remote MCP server (HTTP)
        "github": {
            "type": "http",
            "url": "https://api.githubcopilot.com/mcp/",
            "headers": {"Authorization": "Bearer ${GH_AW_MAIN_REPO_TOKEN}"},
            "tools": ["*"],
        },
    })

    response = await session.send_and_wait("List my recent GitHub notifications", timeout=120)
    print(response.data.content)

    await client.stop()

asyncio.run(main())