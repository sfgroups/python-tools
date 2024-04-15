from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.folder import Folder

# Set your SharePoint site URL
site_url = "https://your-sharepoint-site.sharepoint.com/sites/your-site"

# Set your SharePoint folder URL
folder_url = "/sites/your-site/Shared Documents/FolderName"

# Set your SharePoint username and password
username = "your_username@yourdomain.com"
password = "your_password"

# Initialize AuthenticationContext
auth_context = AuthenticationContext(site_url)
if auth_context.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, auth_context)

    # Check if the folder exists
    folder = ctx.web.get_folder_by_server_relative_url(folder_url)
    ctx.load(folder)
    ctx.execute_query()

    if folder.exists:
        # Remove folder and its subdirectories
        folder.delete_object()
        ctx.execute_query()
        print("Folder and subdirectories removed successfully.")
    else:
        print("Folder does not exist.")
else:
    print("Failed to authenticate.")
