async def milliseconds_to_hh_mm_ss(milliseconds):
    # Convert milliseconds to seconds
    total_seconds = int(milliseconds) // 1000
    
    # Calculate hours, minutes, and remaining seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Format as "hh:mm:ss"
    formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    
    return formatted_time