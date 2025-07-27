import psutil # type: ignore

def get_cpu_usage():
    return psutil.cpu_percent(interval=None)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_network_usage():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv
    }