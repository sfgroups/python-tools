// Check if the incident has the required information to resolve
if (!current.close_notes) {
    gs.addErrorMessage("Please provide resolution notes before resolving the incident.");
    action.setRedirectURL(current);
    return;
}

// Update the incident state and resolution details
current.state = 6; // Resolved state
current.close_notes = current.close_notes || "Resolved via UI Action";
current.update();

// Provide user feedback
gs.addInfoMessage("The incident has been resolved.");

// Redirect back to the incident form
action.setRedirectURL(current);
