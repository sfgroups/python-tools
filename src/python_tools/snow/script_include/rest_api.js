var APIClient = Class.create();
APIClient.prototype = {
    initialize: function() {},

    // Method to make an API call
    callAPI: function(endpoint, payload) {
        try {
            // Retrieve credentials from the Credential Store
            var credentialID = 'INSERT_CREDENTIAL_SYS_ID'; // Replace with the sys_id of the credential
            var creds = this.getCredentials(credentialID);

            if (!creds) {
                gs.error("Failed to retrieve credentials for REST API call.");
                return { error: "Unable to retrieve credentials." };
            }

            // Initialize RESTMessageV2
            var request = new sn_ws.RESTMessageV2();
            request.setEndpoint(endpoint);
            request.setHttpMethod('POST'); // Use POST, GET, PUT, or DELETE as needed

            // Set Basic Auth credentials
            request.setBasicAuth(creds.username, creds.password);

            // Set Request Headers
            request.setRequestHeader('Content-Type', 'application/json');

            // Set Request Body (for POST/PUT)
            if (payload) {
                request.setRequestBody(JSON.stringify(payload));
            }

            // Execute the API call
            var response = request.execute();
            return {
                status: response.getStatusCode(),
                body: response.getBody()
            };

        } catch (ex) {
            gs.error("Error in API call: " + ex.message);
            return { error: ex.message };
        }
    },

    // Helper function to get credentials from Credential Store
    getCredentials: function(credentialID) {
        var gr = new GlideRecord('discovery_credentials');
        if (gr.get(credentialID)) {
            return {
                username: gr.username,
                password: new GlideEncrypter().decrypt(gr.password)
            };
        }
        return null;
    },

    type: 'APIClient'
};
///======
var client = new APIClient();
var apiEndpoint = "https://example.com/api/resource";
var payload = {
    key1: "value1",
    key2: "value2"
};

var result = client.callAPI(apiEndpoint, payload);

if (result.error) {
    gs.error("API Error: " + result.error);
} else {
    gs.info("API Response: " + result.body);
}
