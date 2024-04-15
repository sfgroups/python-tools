import pytest
from unittest.mock import patch
from your_script_name import remove_sharepoint_folder


# Mocking the SharePoint folder object
@patch('your_script_name.Folder')
def test_remove_folder_exists(mock_folder):
    mock_folder.exists = True

    # Mocking the ClientContext
    with patch('your_script_name.ClientContext') as mock_client_context:
        mock_context_instance = mock_client_context.return_value
        remove_sharepoint_folder("https://your-sharepoint-site.sharepoint.com/sites/your-site",
                                 "your_username@yourdomain.com", "your_password",
                                 "/sites/your-site/Shared Documents/FolderName")
        mock_context_instance.web.get_folder_by_server_relative_url.assert_called_once_with(
            "/sites/your-site/Shared Documents/FolderName")
        mock_context_instance.execute_query.assert_called_once()
        mock_folder.delete_object.assert_called_once()
        mock_context_instance.execute_query.assert_called_with()


@patch('your_script_name.Folder')
def test_remove_folder_not_exists(mock_folder):
    mock_folder.exists = False

    # Mocking the ClientContext
    with patch('your_script_name.ClientContext') as mock_client_context:
        mock_context_instance = mock_client_context.return_value
        remove_sharepoint_folder("https://your-sharepoint-site.sharepoint.com/sites/your-site",
                                 "your_username@yourdomain.com", "your_password",
                                 "/sites/your-site/Shared Documents/FolderName")
        mock_context_instance.web.get_folder_by_server_relative_url.assert_called_once_with(
            "/sites/your-site/Shared Documents/FolderName")
        mock_context_instance.execute_query.assert_called_once()
        mock_folder.delete_object.assert_not_called()
        mock_context_instance.execute_query.assert_not_called()


if __name__ == "__main__":
    pytest.main()
