print(f'Invoking __init__.py for {__name__}')

import cx_Oracle

class NmvpsMerger(object):

    def connect(self):
        con = cx_Oracle.connect('nmvpssvc/anf1892@db-corq/corq')
        print("Connection Version -->" , con.version)
        con.close()

    def run_merge(self):
        con = cx_Oracle.connect('nmvpssvc/anf1892@db-corp/corp')
        cur = con.cursor()
        cur.execute('select * from nmvps.vend_chal_evnt where rownum < 10 order by 1')
        for result in cur:
            print(result)
        cur.close()
        con.close()