# coding=utf-8

import os
import time

source = ['D:\\g_GitRepository\\p_PythonCode', 'D:\\g_GitRepository\\p_PythonCode\\bak_src']
target_dir = 'D:\\g_GitRepository\\p_PythonCode\\bak_dst'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment:')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' \
    + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

print target

zip_command = 'HaoZipC a -rtzip %s %s' %(target, ' '.join(source))

print zip_command

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed.'