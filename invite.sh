#!/bin/bash

# Adds users to an organization from a CSV input list.
#
# Usage:
#   Step 1: Create a CSV file with one GitHub username per line.
#           (Ensure there is a trailing newline at the end of the file.)
#   Step 2: ./add-users-to-org-from-list.sh users.csv <org>
#
# Note: This script retrieves each user's numeric GitHub ID and sends an invitation
#       to the organization via the GitHub API.
#
# Requirements:
#   - GitHub CLI (gh) installed and authenticated with sufficient permissions.
#   - jq installed (for JSON payload construction).

if [ $# -lt 2 ]; then
    echo "Usage: $0 <users-file-name> <org>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "File $1 does not exist"
    exit 1
fi

filename="$1"
org="$2"

while read -r username; do
    # Remove any carriage return characters
    username=$(echo "$username" | tr -d '\r')
    
    # Skip empty lines
    if [ -z "$username" ]; then
        continue
    fi

    echo "Inviting user: $username"

    # Retrieve the GitHub numeric ID for the user (trim any trailing newline)
    id=$(gh api users/"$username" --jq '.id' | tr -d '\n')
    if [ -z "$id" ]; then
        echo "Failed to retrieve ID for $username. Skipping."
        continue
    fi

    echo "User $username has numeric ID: $id"
    
    # Build JSON payload with invitee_id as a number using jq
    payload=$(jq -n --argjson id "$id" '{invitee_id: $id}')
    
    # Send the invitation to the organization
    response=$(echo "$payload" | gh api --method POST \
      -H "Accept: application/vnd.github+json" \
      "/orgs/$org/invitations" --input -)
    
    echo "Response for $username: $response"
done < "$filename"
