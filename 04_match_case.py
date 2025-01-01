def https_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "done"
        case 500:
            return "internal server error"
        case _:
            return "unknow status"

print(https_status(200))
print(https_status(404))
print(https_status(500) )
print(https_status(5423 ))
