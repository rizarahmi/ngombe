#!/usr/bin/env python3
"""Ubah struk jadi kertas thermal 58mm.  Pemakaian: python3 patch-58mm.py index.html"""
import sys, shutil
path = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
src = open(path, encoding='utf-8').read()

edits = [
 (".receipt{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;background:#fff;color:#111;padding:16px;border-radius:12px;border:1px dashed #bbb;max-width:320px;margin:0 auto}",
  ".receipt{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:11px;line-height:1.35;background:#fff;color:#000;padding:3mm 4mm;border-radius:6px;border:1px dashed #bbb;width:58mm;max-width:100%;margin:0 auto;overflow-wrap:anywhere}"),
 (".receipt .r-logo{display:block;width:150px;margin:0 auto 6px}",
  ".receipt .r-logo{display:block;width:38mm;max-width:100%;margin:0 auto 6px}"),
 ("""@media print{
  body *{visibility:hidden}
  #receipt,#receipt *{visibility:visible}
  #receipt{position:absolute;left:0;top:0;width:58mm;border:0;padding:0;max-width:none}
  .modal{background:none}
}""",
  """@page{size:58mm auto;margin:0}
@media print{
  html,body{width:58mm;margin:0;padding:0;background:#fff}
  .topbar,main,.login,.toast,.scrim,.cart-fab,.modal-head,.modal-foot,.done-mark{display:none!important}
  .modal{position:static;display:block;padding:0;background:none}
  .modal-card{max-width:none;max-height:none;overflow:visible;border-radius:0;background:none}
  .modal-body{padding:0;overflow:visible}
  .receipt{width:58mm;max-width:none;margin:0;border:0;border-radius:0;padding:2mm 4mm 6mm;font-size:11px}
}"""),
]
for old, new in edits:
    n = src.count(old)
    if n != 1:
        sys.exit('Gagal: bagian ditemukan %d kali (harus 1):\n%s' % (n, old[:80]))
    src = src.replace(old, new)
shutil.copyfile(path, path + '.bak58')
open(path, 'w', encoding='utf-8').write(src)
print('Selesai: struk sekarang 58mm.')
