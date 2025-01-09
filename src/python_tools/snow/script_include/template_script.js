(function executeRule(current, previous /*null when async*/) {
    try {
        gs.debug("Starting Business Rule execution");
        gs.info("Current Sys ID: " + current.sys_id);

        if (!current.active) {
            gs.warn("Record is not active, skipping processing");
            return;
        }

        // Simulate some logic
        var result = someFunction();
        gs.info("Function result: " + result);

    } catch (e) {
        gs.error("Error in Business Rule: " + e.message);
    }
})(current, previous);
