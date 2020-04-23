import pymem
import re

pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'client_panorama.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'\x81\xE2.{4}\x84\xDB',
                                         clientModule).start() + 4

pm.write_uchar(address, 0x42 if pm.read_uchar(address) == 0x2 else 0x2)
pm.close_process()
