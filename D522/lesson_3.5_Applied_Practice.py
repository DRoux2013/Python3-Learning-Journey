import shutil
import os
#shutil.copytree('/home/davidlaroux/network_cleanup_lab/configs', '/home/davidlaroux/network_cleanup_lab/configs_backup')
os.rename('/home/davidlaroux/network_cleanup_lab/configs/router1.cfg', '/home/davidlaroux/network_cleanup_lab/configs/router1_config.txt')
os.rename('/home/davidlaroux/network_cleanup_lab/configs/switch1.cfg', '/home/davidlaroux/network_cleanup_lab/configs/switch1_config.txt')
os.mkdir('/home/davidlaroux/network_cleanup_lab/configs/archived')
shutil.move('/home/davidlaroux/network_cleanup_lab/configs/old_firewall.cfg', '/home/davidlaroux/network_cleanup_lab/configs/archived' )
shutil.rmtree('/home/davidlaroux/network_cleanup_lab/configs/temp/')