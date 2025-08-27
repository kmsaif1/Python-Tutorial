def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500:
            return "Internet server error"
        case _:
            return "Unknown Status"
        
print (http_status(200))
