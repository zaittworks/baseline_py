def convert_units(all_inputs):

  input_value = all_inputs['value_input']
  convert_from = all_inputs['from_input']
  convert_to = all_inputs['to_input']
  
  sql_where = "WHERE ([convert_from] = '" + str(convert_from) + "' OR [convert_from_short] = '" + \
              str(convert_from) + "') AND ([convert_to] = '" + str(convert_to) + "' OR [convert_to_short] = '" + str(convert_to) + "')"

  import sqlite3
  db_path = 'E:\\zaitt.works\\Reel\\baseline.py\\unit_converter.db'
  database_connection = sqlite3.connect(db_path)
  database_cursor = database_connection.cursor()
  database_cursor.execute('SELECT [convert_from], [convert_to], [factor] FROM [conversion_factors] ' + sql_where + ';')
  found_data = database_cursor.fetchall()

  if len(found_data) > 0:
    conversion_factor = float(found_data[0][2])
    from_unit = str(found_data[0][0])
    to_unit = str(found_data[0][1])

    conversion_type = str(from_unit) + '-' + str(to_unit)
    conversion_value = float(input_value)

    string_output = '{conv_type}: {conv_value:.3f}'.format(conv_type=conversion_type, conv_value=conversion_value * conversion_factor)

  else:
    string_output = 'your inputs don\'t make any sense'

  function_outputs = dict()
  function_outputs['sql_where'] = sql_where
  function_outputs['conversion_type'] = conversion_type
  function_outputs['conversion_value'] = conversion_value
  function_outputs['string_output'] = string_output

  return function_outputs
