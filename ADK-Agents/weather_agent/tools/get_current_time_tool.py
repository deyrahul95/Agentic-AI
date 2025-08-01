from datetime import datetime

def get_current_time() -> dict:
    """Retrieves the current time in '%H:%M:%S' format.

    Returns:
        dict: A dictionary containing the current time in '%H:%M:%S' format.

        Example:
            {
                "current_time": "17:42:13"
            }
    """

    now = datetime.now()

    return {
        "current_time": now.strftime("%H:%M:%S")
    }
