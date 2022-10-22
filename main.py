import user_interface as ui
import logger as lg
import crud as cr

lg.logging.info('Start')
cr.init_data_base('phone_base.csv')
ui.ls_menu()
