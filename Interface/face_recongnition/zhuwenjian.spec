# -*- mode: python -*-

block_cipher = None


a = Analysis(['zhuwenjian.py'],
             pathex=['add_teacher.py', 'admin.py', 'chazhao_id.py', 'create_table.py', 'face.py', 'face_re.py', 'grade.py', 'hello.py', 'insert_db.py', 'stu_adds.py', 'TC_info.py', 'test.py', 'tijiaocg.py', 'tmysql.py', 'tool.py', 'x_g_stu.py', 'x_g_stu_two.py', 'Xs.py', 'xuesheng_tijiao.py', '/home/xms/桌面/check_face'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='zhuwenjian',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
