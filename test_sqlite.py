
import futil as f


# Since root no path needed:

db_name = 'test_regnr_db.db'

conx = f.CheckReg(db_name)

print(conx.n_tables())
print(conx.check_reg('reg_nr_tbl', 'regnr', 'DK123'))

print(conx.check_reg('reg_nr_tbl', 'regnr', 'DK12345'))


db_name = 'ok_db_test.db'

conx = f.CheckReg(db_name)

print(conx.n_tables())

tab_name = 'okq8_tbl'

print(conx.check_reg(tab_name, 'regnr', 'DK123'))
