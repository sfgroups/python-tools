(function executeRule(current, previous /*null when async*/) {
    try {
        // Initialize the RESTMessageV2 object
        var request = new sn_ws.RESTMessageV2();
        request.setEndpoint('https://' + gs.getProperty('instance_name') + '.service-now.com/api/now/v1/batch');
        request.setHttpMethod('POST');

        // Set headers
        request.setRequestHeader('Content-Type', 'application/json');
        request.setBasicAuth('username', 'password'); // Replace with your credentials

        // Batch payload to create DPR release
        var payload = {
            batch_requests: [
                {
                    method: "POST",
                    url: "/api/now/table/sn_dpr_model_release",
                    headers: { "Content-Type": "application/json" },
                    body: {
                        name: current.release_name || "Default Release Name",
                        product_version: current.product_version || "1.0",
                        product_owner: current.product_owner || "Default Owner",
                        state: "Pending",
                        status: "green",
                        release_template: "Deployment",
                        planned_start_date: current.planned_start_date || new GlideDateTime().getDisplayValue(),
                        planned_end_date: current.planned_end_date || new GlideDateTime().addDays(30).getDisplayValue(),
                        description: current.description || "Created via Business Rule"
                    }
                }
            ]
        };

        // Set the request body
        request.setRequestBody(JSON.stringify(payload));

        // Execute the batch API call
        var response = request.execute();
        var httpStatus = response.getStatusCode();
        var responseBody = response.getBody();

        // Log results for debugging
        gs.info("Batch API HTTP Status: " + httpStatus);
        gs.info("Batch API Response: " + responseBody);

        // Optionally process the response
        if (httpStatus === 200) {
            gs.addInfoMessage("DPR Release created successfully.");
        } else {
            gs.addErrorMessage("Failed to create DPR Release. Check logs for details.");
        }
    } catch (ex) {
        gs.error("Error in Business Rule: " + ex.message);
    }
})(current, previous);
