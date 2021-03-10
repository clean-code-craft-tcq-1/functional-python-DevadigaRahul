ranges ={
  'temp':{'min':1,'max':45},#Temperature
  'soc':{'min':20,'max':80},#state of Charge
  'charge_rate':{'min':0,'max':0.8},#state of Charge
  }
test_report=[]
test_case_id=0

def append_list(src_list,dst_list):
    for x in src_list:
      dst_list.append(x)  

def min_range_test(value,range_min):
  result=False #Test step pass->Normal behavior
  test_step='\t\tTeststep::Passed ->Actual value:'+str(value)+' is greater than Min Range:'+str(range_min)
  if value < range_min:
    test_step='\t\tTeststep::Failed ->Actual value:'+str(value)+' is less than Min Range:'+str(range_min)
    result=True #Test step failed->abnormal behavior
  return test_step,result

def max_range_test(value,range_max):
  result=False #Test step pass->Normal behavior
  test_step='\t\tTeststep::Passed ->Actual value:'+str(value)+' is less than Max Range:'+str(range_max)
  if value > range_max:
    test_step='\t\tTeststep::Failed ->Actual value:'+str(value)+' is greater than Max Range:'+str(range_max)
    result=True #Test step failed->abnormal behavior
  return test_step,result

def collect_abnormals(abnormals,test_case_report,attribute_name,attribute_value,attribute_range):

  result=False #Test attribute is within Min and Max range->Normal behavior

  test_step_min,min_range_result=min_range_test(attribute_value,attribute_range['min'])#test for min range
  test_step_max,max_range_result=max_range_test(attribute_value,attribute_range['max'])#test for max range
  
  if min_range_result or max_range_result:
    result=True #Test attribute is not within Min and Max range->abnormal behavior
    abnormals.append(attribute_name)
  return [test_step_min,test_step_max],result


def report_abnormals_attribute(attribute_report):
  abnormals=[]
  test_case_report=[]

  for attribute in attribute_report:
    report='\tTest Attribute['+attribute+']::->Passed'#Test attribute is within Min and Max range->Normal behavior
    test_step,result=collect_abnormals(abnormals,test_case_report,attribute,attribute_report[attribute],ranges[attribute])
    if result==True:
      report='\tTest Attribute['+attribute+']::->Failed' #Test attribute is not within Min and Max range->abnormal behavior
    test_case_report.append(report)
    append_list(test_step,test_case_report)
  return test_case_report,abnormals

def test_abnormals_attribute(battery_report):

  global test_case_id
  test_case_id+=1
  test_case='Test Case ID['+str(test_case_id)+"]->Passed"
  test_step,abnormals=report_abnormals_attribute(battery_report)
  if(len(abnormals)!=0):
    test_case='Test Case ID::['+str(test_case_id)+"]->Failed"
  test_report.append(test_case)
  append_list(test_step,test_report)
  #assert(len(abnormals)==0)


if __name__ == '__main__':
  test_input_battery_report_1 ={
    'temp':25,
    'soc':70,
    'charge_rate':0.7
    }
  test_input_battery_report_2 ={
    'temp':0,
    'soc':85,
    'charge_rate':0.9
    }
  test_abnormals_attribute(test_input_battery_report_1)
  test_abnormals_attribute(test_input_battery_report_2)
  test_abnormals_attribute(test_input_battery_report_1)
  
  for line in test_report:
    print(line)
