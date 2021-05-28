import osudb

def Merge_collection(base, update):
        CDB_Base = osudb.parse_collection(base)
        CDB_Update = osudb.parse_collection(update)
        for i in range(0,len(CDB_Update[2])):
            found = False
            for bcollection in CDB_Base[2]:
                if CDB_Update[2][i][0] in bcollection:
                    found = True
                    CDB_Base[2][CDB_Base[2].index(bcollection)][2] = list(set(CDB_Base[2][CDB_Base[2].index(bcollection)][2]) | set(CDB_Update[2][i][2]))
                    CDB_Base[2][CDB_Base[2].index(bcollection)][1] = len(CDB_Base[2][CDB_Base[2].index(bcollection)][2])
            if not found: 
                CDB_Base[2].append(CDB_Update[2][i])
                CDB_Base[1] += 1
                print("Added:",CDB_Update[2][i],"(type:Collection)")
        return CDB_Base

