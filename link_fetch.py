import re

def get_main_name(url):
  """Fetches the main name from a URL.

  Args:
      url: The URL string.

  Returns:
      The main name of the URL, or None if the URL is invalid.
  """

  # Check if the URL starts with "http://" or "https://"
  if not re.match(r"^(http|https)://", url):
    return None

  # Use regular expression to capture everything before the first dot or path separator
  match = re.search(r"(https?://)?(www\d?\.)?([^/\.]+)", url)

  # Check if there's a match
  if not match:
    return None

  # Return the captured main name
  return match.group(3)

# Example usage
url = "https://rkehs.edu.bd"
main_name = get_main_name(url)

if main_name:
  print(f"Main name: {main_name}")
else:
  print("Invalid URL or no main name found.")
