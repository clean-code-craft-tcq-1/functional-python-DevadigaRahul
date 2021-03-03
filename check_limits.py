ranges ={
  'temp':{'min':0,'max':45},#Temperature
  'soc':{'min':20,'max':80},#state of Charge
  'charge_rate':{'min':0,'max':0.8},#state of Charge
  }
test_report=[]
def collect_abnormals(abnormals,attribute_name,attribute_value,attribute_range):
  if attribute_value < attribute_range['min'] or attribute_value > attribute_range['max']:
    report="Attribute:"+attribute_name +"Actual value:"+str(attribute_value)+"[Expected Range::Min:"+str(attribute_range['min'])+"::Max:"+str(attribute_range['max'])
    abnormals.append(report)


def report_abnormals_attribute(attribute_report):
  abnormals=[]
  for attribute in attribute_report:
    collect_abnormals(abnormals,attribute,attribute_report[attribute],ranges[attribute])
  return abnormals

def test_abnormals_attribute(battery_report):
  
  '''for line in report_abnormals_attribute(battery_report):
    print(line)
  assert(len(report_abnormals_attribute(battery_report))==0)'''
  test_report.append(report_abnormals_attribute(battery_report))

'''def battery_is_ok(temperature, soc, charge_rate):
  if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  elif soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  elif charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False

  return True'''


if __name__ == '__main__':
  '''assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)'''
  test_input_battery_report_1 ={
    'temp':25,
    'soc':70,
    'charge_rate':0.7
    }
  test_input_battery_report_2 ={
    'temp':25,
    'soc':85,
    'charge_rate':0.9
    }
  test_abnormals_attribute(test_input_battery_report_1)
  test_abnormals_attribute(test_input_battery_report_2)
  
  print(test_report)
