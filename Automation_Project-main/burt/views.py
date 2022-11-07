from multiprocessing import context
from django.shortcuts import render, redirect
from .models import QueryHolder, HelperModel
import json
import requests

url = 'https://qtest.eng.netapp.com'
projectId = 67

def new_home(request):
    if request.method == 'POST':
        type_new_modify = request.POST.get('type_new_modify')
        report_name = request.POST.get('report_name')
        if type_new_modify == 'new':
            return render(request, 'burt/home.html')
        else:
            pass
    else:
        return render(request, 'burt/new_home.html')


def QTestHandler(query):
    # token = ''

    # payload='grant_type=password&username=cse_automation@netapp.com&password=NetApp1!'
    # headers1 = {
    # 'Authorization': 'Basic Y3NlX2F1dG9tYXRpb25AbmV0YXBwLmNvbTo=',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'qtest-8080=s15'
    # }
    # r = requests.request('POST', f'{url}/oauth/token', data=payload, headers=headers1)
    # token = r.json()['access_token']

    # headers2 = {
    #     'Authorization': f'bearer {token}',
    #     'Content-Type': 'application/json'
    # }
    # data = {
    # "object_type": "test-runs",
    # "fields": ["*"],
    # "query": query
    # } 

    # r = requests.request('POST', f'{url}/api/v3/projects/{projectId}/search', headers=headers2, data=json.dumps(data))
    # print(r.json())

    data123 = {'items': [
        {
            'parentId': 16674,
            'parentType': 'test-suite',
            'automation': 'Yes',
            'testCaseId': 524837,
            'links': [
                {
                    'rel': 'test-case',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524837?versionId=827207&showParamIdentifier=false'
                },
                {
                    'rel': 'test-cycle',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684'
                },
                {
                    'rel': 'test-suite',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674'
                },
                {
                    'rel': 'self',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247386'
                }
            ],
            'id': 247386,
            'name': 'PVT_NIC_RSSv4_Singlemode_Ifgrp',
            'order': 1,
            'pid': 'TR-5',
            'created_date': '2017-12-11T06:48:30+00:00',
            'last_modified_date': '2021-03-18T10:24:44+00:00',
            'properties': [
                {
                    'field_id': 7096,
                    'field_name': 'Run Order',
                    'field_value': '1'
                },
                {
                    'field_id': 7086,
                    'field_name': 'Execution Type',
                    'field_value': '501',
                    'field_value_name': 'Functional'
                },
                {
                    'field_id': 7094,
                    'field_name': 'Planned Start Date',
                    'field_value': '2017-10-27T00:00:00+00:00'
                },
                {
                    'field_id': 7097,
                    'field_name': 'Status',
                    'field_value': '601',
                    'field_value_name': 'Passed'
                },
                {
                    'field_id': 7093,
                    'field_name': 'Planned End Date',
                    'field_value': '2017-10-27T00:00:00+00:00'
                },
                {
                    'field_id': 7101,
                    'field_name': 'Build Version',
                    'field_value': ''
                },
                {
                    'field_id': 7077,
                    'field_name': 'Assigned To',
                    'field_value': '473',
                    'field_value_name': 'Amit Haval'
                },
                {
                    'field_id': 7102,
                    'field_name': 'Controllers Used',
                    'field_value': ''
                },
                {
                    'field_id': 7103,
                    'field_name': 'BURT',
                    'field_value': ''
                },
                {
                    'field_id': 7104,
                    'field_name': 'Incidents',
                    'field_value': ''
                },
                {
                    'field_id': 10950,
                    'field_name': 'Runtime',
                    'field_value': ''
                },
                {
                    'field_id': 10980,
                    'field_name': 'Time To First Failure',
                    'field_value': ''
                },
                {
                    'field_id': 11010,
                    'field_name': 'Expected Runtime',
                    'field_value': ''
                },
                {
                    'field_id': 7138,
                    'field_name': 'Keywords',
                    'field_value': ''
                },
                {
                    'field_id': 7108,
                    'field_name': 'Systemic Ratchet Level',
                    'field_value': '',
                    'field_value_name': ''
                },
                {
                    'field_id': 7109,
                    'field_name': 'NATE LOG URL',
                    'field_value': ''
                },
                {
                    'field_id': 7139,
                    'field_name': 'ONTAP Mode',
                    'field_value': '',
                    'field_value_name': ''
                },
                {
                    'field_id': 7110,
                    'field_name': 'Pass Rate',
                    'field_value': ''
                },
                {
                    'field_id': 7140,
                    'field_name': 'Executing Subteam',
                    'field_value': '44',
                    'field_value_name': 'PLTE'
                },
                {
                    'field_id': 7141,
                    'field_name': 'Product Models',
                    'field_value': '',
                    'field_value_name': ''
                },
                {
                    'field_id': 7111,
                    'field_name': 'QC_APP_NAME',
                    'field_value': ''
                },
                {
                    'field_id': 7112,
                    'field_name': 'Duration',
                    'field_value': ''
                },
                {
                    'field_id': 7114,
                    'field_name': 'NATE_UUID',
                    'field_value': ''
                },
                {
                    'field_id': 7115,
                    'field_name': 'Description',
                    'field_value': ''
                },
                {
                    'field_id': 7113,
                    'field_name': 'ZAPI Input',
                    'field_value': ''
                },
                {
                    'field_id': 17618,
                    'field_name': 'CTL Execution ID',
                    'field_value': ''
                },
                {
                    'field_id': 17619,
                    'field_name': 'SITE',
                    'field_value': ''
                },
                {
                    'field_id': 17620,
                    'field_name': 'NATE TOP LOGDIR',
                    'field_value': ''
                }
            ],
            'test_case': {
                'links': [
                ],
                'id':524837,
                'test_case_version_id':827207,
                'agent_ids':[
                ]
            },
            'latest_test_log':{
                'status': 'Passed',
                'id': 44162,
                'exe_start_date': '2017-12-14T09:24:34+00:00',
                'exe_end_date': '2017-12-14T09:24:34+00:00'
            },
            'test_case_version_id': 827207,
            'test_case_version': '3.0',
            'creator_id': 473
        },
        {
            'parentId': 16674,
            'parentType': 'test-suite',
            'automation': 'No',
            'testCaseId': 524838,
            'links': [
                {
                    'rel': 'test-case',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524838?versionId=827208&showParamIdentifier=false'
                },
                {
                    'rel': 'test-cycle',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684'
                },
                {
                    'rel': 'test-suite',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674'
                },
                {
                    'rel': 'self',
                    'href': 'https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247387'
                }
            ],
            'id': 247387,
            'name': 'PVT_NIC_RSSv4_Multimode_Ifgrp',
            'order': 2,
            'pid': 'TR-6',
            'created_date': '2017-12-14T09:24:34+00:00',
            'last_modified_date': '2021-03-18T10:24:44+00:00',
            'properties': [
                {
                    'field_id': 7096,
                    'field_name': 'Run Order',
                    'field_value': '2'
                },
                {
                    'field_id': 7086,
                    'field_name': 'Execution Type',
                    'field_value': '501',
                    'field_value_name': 'Functional'
                },
                {
                    'field_id': 7094,
                    'field_name': 'Planned Start Date',
                    'field_value': '2017-10-27T00:00:00+00:00'
                },
                {
                    'field_id': 7097,
                    'field_name': 'Status',
                    'field_value': '601',
                    'field_value_name': 'Passed'
                },
                {
                    'field_id': 7093,
                    'field_name': 'Planned End Date',
                    'field_value': '2017-10-27T00:00:00+00:00'
                },
                {
                    'field_id': 7101,
                    'field_name': 'Build Version',
                    'field_value': ''
                },
                {
                    'field_id': 7077,
                    'field_name': 'Assigned To',
                    'field_value': '473',
                    'field_value_name': 'Amit Haval'
                },
                {
                    'field_id': 7102,
                    'field_name': 'Controllers Used',
                    'field_value': ''
                },
                {
                    'field_id': 7103,
                    'field_name': 'BURT',
                    'field_value': ''
                },
                {
                    'field_id': 7104,
                    'field_name': 'Incidents',
                    'field_value': ''
                },
                {
                    'field_id': 10950,
                    'field_name': 'Runtime',
                    'field_value': ''
                },
                {
                    'field_id': 10980,
                    'field_name': 'Time To First Failure',
                    'field_value': ''
                },
                {
                    'field_id': 11010,
                    'field_name': 'Expected Runtime',
                    'field_value': ''
                },
                {
                    'field_id': 7138,
                    'field_name': 'Keywords',
                    'field_value': ''
                },
                {
                    'field_id': 7108,
                    'field_name': 'Systemic Ratchet Level',
                    'field_value': '',
                    'field_value_name': ''
                },
                {
                    'field_id': 7109,
                    'field_name': 'NATE LOG URL',
                    'field_value': ''
                },
                {
                    'field_id': 7139,
                    'field_name': 'ONTAP Mode',
                    'field_value': '',
                    'field_value_name': ''
                },
                {
                    'field_id': 7110,
                    'field_name': 'Pass Rate',
                    'field_value': ''
                },
                {
                    'field_id': 7140,
                    'field_name': 'Executing Subteam',
                    'field_value': '',
                    'field_value_name': ''
                },
                {
                    'field_id': 7141,
                    'field_name': 'Product Models',
                    'field_value': '',
                    'field_value_name': ''
                },
                {
                    'field_id': 7111,
                    'field_name': 'QC_APP_NAME',
                    'field_value': ''
                },
                {
                    'field_id': 7112,
                    'field_name': 'Duration',
                    'field_value': ''
                },
                {
                    'field_id': 7114,
                    'field_name': 'NATE_UUID',
                    'field_value': ''
                },
                {
                    'field_id': 7115,
                    'field_name': 'Description',
                    'field_value': ''
                },
                {
                    'field_id': 7113,
                    'field_name': 'ZAPI Input',
                    'field_value': ''
                },
                {
                    'field_id': 17618,
                    'field_name': 'CTL Execution ID',
                    'field_value': ''
                },
                {
                    'field_id': 17619,
                    'field_name': 'SITE',
                    'field_value': ''
                },
                {
                    'field_id': 17620,
                    'field_name': 'NATE TOP LOGDIR',
                    'field_value': ''
                }
            ],
            'test_case': {
                'links': [
                ],
                'id':524838,
                'test_case_version_id':827208,
                'agent_ids':[
                ]
            },
            'latest_test_log':{
                'status': 'Passed',
                'id': 44163,
                'exe_start_date': '2017-12-14T09:24:34+00:00',
                'exe_end_date': '2017-12-14T09:24:34+00:00'
            },
            'test_case_version_id': 827208,
            'test_case_version': '3.0',
            'creator_id': 473
        }]}


    
    data_header = ["ID", "NAME", "STATUS", "TYPE", "VERSION"]
    return data123['items'], data_header

def home(request):
    if request.method == 'POST':
        query = request.POST.get('query_select')
        num_of_tables = request.POST.get('num_of_tables')
        number_of_rows = request.POST.get('number_of_rows')
        number_of_columns = request.POST.get('number_of_columns')
        if query == 'burt':
            return redirect(f'/query_boss/{num_of_tables}/{number_of_rows}/{number_of_columns}')
        elif query == 'Jira':
            pass
        elif query == 'QTest':
            return redirect('q_test')
    else:
        return render(request, 'burt/home.html')


def q_test(request):
    query = ''
    if request.method == 'POST':
        query = request.POST.get('query')
    data, data_header = QTestHandler(query)

    return render(request, 'burt/QTest.html', {"data":data, "header": data_header, "query": query})


def query_boss(request, num_of_tables, number_of_rows, number_of_columns):
    if request.method == 'POST':
        keywords = []
        for i in range(number_of_columns):
            keywords.append(request.POST.get(f'keyword{i}'))
        names = []
        new = []
        for i in range(int(num_of_tables)):
            name = request.POST.get(f'name_{i+1}')

            query_ = request.POST.get(f'q_{i+1}')
            print(query_)

            # counting for every keyword then keeping the result inside res dict
            result = send_req_get_data(query_).lower()
            print('result: '+result)
            tmp_dict = {}
            for word in keywords:
                tmp = result.count(word.lower())
                tmp_dict[f'{word}'] = tmp
            if name not in names:
                names.append(name)
                new.append([name, tmp_dict])
            else:
                for item in new:
                    if name in item[0]:
                        for w in keywords:
                            item[1][w] = item[1][w] + tmp_dict[w]
                        break
            print(new)
        context = {
            'result': new,
            'keywords': keywords
        }

        return render(request, 'burt/new_result.html', context)

    else:
        my_list = []
        for i in range(int(num_of_tables)):
            my_list.append(i+1)
        context = {
            'list_': my_list,
            'num_of_queries': num_of_tables,
            'number_of_rows': range(number_of_rows),
            'number_of_columns': range(number_of_columns)
        }
        return render(request, 'burt/query_boss.html', context)


def burt_(request):
    if request.method == 'POST':
        open_new = request.POST.get('open_new')
        test_me = request.POST.get('test_me')
        study = request.POST.get('study')
        fixed = request.POST.get('fixed')
        closed = request.POST.get('closed')
        multistate = request.POST.get('multistate')

        if 'submit' in request.POST:
            open_new = send_req_get_data(open_new).lower()
            test_me = send_req_get_data(test_me).lower()
            study = send_req_get_data(study).lower()
            fixed = send_req_get_data(fixed).lower()
            closed = send_req_get_data(closed).lower()
            multistate = send_req_get_data(multistate).lower()

            # 0=new/open 1=testme 2=study 3=fixed 4=closed 5=multistate
            Dg2Au = [0, 0, 0, 0, 0, 0]
            Dg2Au[0] = Dg2Au[0] + open_new.count('new')
            Dg2Au[0] = Dg2Au[0] + open_new.count('open')
            Dg2Au[1] = Dg2Au[1] + open_new.count('testme')
            Dg2Au[2] = Dg2Au[2] + open_new.count('study')
            Dg2Au[3] = Dg2Au[3] + open_new.count('fixed')
            Dg2Au[4] = Dg2Au[4] + open_new.count('closed')
            Dg2Au[5] = Dg2Au[5] + open_new.count('multistate')

            Dg2Au[0] = Dg2Au[0] + test_me.count('new')
            Dg2Au[0] = Dg2Au[0] + test_me.count('open')
            Dg2Au[1] = Dg2Au[1] + test_me.count('testme')
            Dg2Au[2] = Dg2Au[2] + test_me.count('study')
            Dg2Au[3] = Dg2Au[3] + test_me.count('fixed')
            Dg2Au[4] = Dg2Au[4] + test_me.count('closed')
            Dg2Au[5] = Dg2Au[5] + test_me.count('multistate')

            Dg2Au[0] = Dg2Au[0] + study.count('new')
            Dg2Au[0] = Dg2Au[0] + study.count('open')
            Dg2Au[1] = Dg2Au[1] + study.count('testme')
            Dg2Au[2] = Dg2Au[2] + study.count('study')
            Dg2Au[3] = Dg2Au[3] + study.count('fixed')
            Dg2Au[4] = Dg2Au[4] + study.count('closed')
            Dg2Au[5] = Dg2Au[5] + study.count('multistate')

            Dg2Au[0] = Dg2Au[0] + fixed.count('new')
            Dg2Au[0] = Dg2Au[0] + fixed.count('open')
            Dg2Au[1] = Dg2Au[1] + fixed.count('testme')
            Dg2Au[2] = Dg2Au[2] + fixed.count('study')
            Dg2Au[3] = Dg2Au[3] + fixed.count('fixed')
            Dg2Au[4] = Dg2Au[4] + fixed.count('closed')
            Dg2Au[5] = Dg2Au[5] + fixed.count('multistate')

            Dg2Au[0] = Dg2Au[0] + closed.count('new')
            Dg2Au[0] = Dg2Au[0] + closed.count('open')
            Dg2Au[1] = Dg2Au[1] + closed.count('testme')
            Dg2Au[2] = Dg2Au[2] + closed.count('study')
            Dg2Au[3] = Dg2Au[3] + closed.count('fixed')
            Dg2Au[4] = Dg2Au[4] + closed.count('closed')
            Dg2Au[5] = Dg2Au[5] + closed.count('multistate')

            Dg2Au[0] = Dg2Au[0] + multistate.count('new')
            Dg2Au[0] = Dg2Au[0] + multistate.count('open')
            Dg2Au[1] = Dg2Au[1] + multistate.count('testme')
            Dg2Au[2] = Dg2Au[2] + multistate.count('study')
            Dg2Au[3] = Dg2Au[3] + multistate.count('fixed')
            Dg2Au[4] = Dg2Au[4] + multistate.count('closed')
            Dg2Au[5] = Dg2Au[5] + multistate.count('multistate')

            # todo: add the same thing for multistate

            obj = HelperModel()
            obj.open_new = Dg2Au[0]
            obj.test_me = Dg2Au[1]
            obj.study = Dg2Au[2]
            obj.fixed = Dg2Au[3]
            obj.closed = Dg2Au[4]
            obj.multistate = Dg2Au[5]
            obj.total = Dg2Au[0] + Dg2Au[1] + \
                Dg2Au[2] + Dg2Au[3] + Dg2Au[4] + Dg2Au[5]
            obj.save()
            return redirect(f'/burt2/{obj.pk}')

        elif 'save' in request.POST:
            # save the query in Database
            # obj = QueryHolder()
            # obj.query = query
            # obj.save()
            return redirect('/burt')
    else:
        return render(request, 'burt/save_or_submit.html')


def burt__(request, pk):
    obj = HelperModel.objects.get(pk=pk)
    if request.method == 'POST':
        open_new = request.POST.get('open_new')
        test_me = request.POST.get('test_me')
        study = request.POST.get('study')
        fixed = request.POST.get('fixed')
        closed = request.POST.get('closed')
        multistate = request.POST.get('multistate')
        open_new = send_req_get_data(open_new).lower()
        test_me = send_req_get_data(test_me).lower()
        study = send_req_get_data(study).lower()
        fixed = send_req_get_data(fixed).lower()
        closed = send_req_get_data(closed).lower()
        multistate = send_req_get_data(multistate).lower()

        # 0=new/open 1=testme 2=study 3=fixed 4=closed 5=multistate
        Dg2Au = [0, 0, 0, 0, 0, 0]
        Dg2Au[0] = Dg2Au[0] + open_new.count('new')
        Dg2Au[0] = Dg2Au[0] + open_new.count('open')
        Dg2Au[1] = Dg2Au[1] + open_new.count('testme')
        Dg2Au[2] = Dg2Au[2] + open_new.count('study')
        Dg2Au[3] = Dg2Au[3] + open_new.count('fixed')
        Dg2Au[4] = Dg2Au[4] + open_new.count('closed')
        Dg2Au[5] = Dg2Au[5] + open_new.count('multistate')

        Dg2Au[0] = Dg2Au[0] + test_me.count('new')
        Dg2Au[0] = Dg2Au[0] + test_me.count('open')
        Dg2Au[1] = Dg2Au[1] + test_me.count('testme')
        Dg2Au[2] = Dg2Au[2] + test_me.count('study')
        Dg2Au[3] = Dg2Au[3] + test_me.count('fixed')
        Dg2Au[4] = Dg2Au[4] + test_me.count('closed')
        Dg2Au[5] = Dg2Au[5] + test_me.count('multistate')

        Dg2Au[0] = Dg2Au[0] + study.count('new')
        Dg2Au[0] = Dg2Au[0] + study.count('open')
        Dg2Au[1] = Dg2Au[1] + study.count('testme')
        Dg2Au[2] = Dg2Au[2] + study.count('study')
        Dg2Au[3] = Dg2Au[3] + study.count('fixed')
        Dg2Au[4] = Dg2Au[4] + study.count('closed')
        Dg2Au[5] = Dg2Au[5] + study.count('multistate')

        Dg2Au[0] = Dg2Au[0] + fixed.count('new')
        Dg2Au[0] = Dg2Au[0] + fixed.count('open')
        Dg2Au[1] = Dg2Au[1] + fixed.count('testme')
        Dg2Au[2] = Dg2Au[2] + fixed.count('study')
        Dg2Au[3] = Dg2Au[3] + fixed.count('fixed')
        Dg2Au[4] = Dg2Au[4] + fixed.count('closed')
        Dg2Au[5] = Dg2Au[5] + fixed.count('multistate')

        Dg2Au[0] = Dg2Au[0] + closed.count('new')
        Dg2Au[0] = Dg2Au[0] + closed.count('open')
        Dg2Au[1] = Dg2Au[1] + closed.count('testme')
        Dg2Au[2] = Dg2Au[2] + closed.count('study')
        Dg2Au[3] = Dg2Au[3] + closed.count('fixed')
        Dg2Au[4] = Dg2Au[4] + closed.count('closed')
        Dg2Au[5] = Dg2Au[5] + closed.count('multistate')

        Dg2Au[0] = Dg2Au[0] + multistate.count('new')
        Dg2Au[0] = Dg2Au[0] + multistate.count('open')
        Dg2Au[1] = Dg2Au[1] + multistate.count('testme')
        Dg2Au[2] = Dg2Au[2] + multistate.count('study')
        Dg2Au[3] = Dg2Au[3] + multistate.count('fixed')
        Dg2Au[4] = Dg2Au[4] + multistate.count('closed')
        Dg2Au[5] = Dg2Au[5] + multistate.count('multistate')
        total = Dg2Au[0] + Dg2Au[1] + Dg2Au[2] + Dg2Au[3] + Dg2Au[4] + Dg2Au[5]
        # todo: add the same thing for multistate
        context = {
            'dg2au': obj,
            'open_new': Dg2Au[0],
            'test_me': Dg2Au[1],
            'study': Dg2Au[2],
            'fixed': Dg2Au[3],
            'closed': Dg2Au[4],
            'multistate': Dg2Au[5],
            'total1': obj.total,
            'total2': total
        }
        return render(request, 'burt/result.html', context)
    else:
        return render(request, 'burt/burt2.html')

# ----helpers---


def send_req_get_data(query):
    import paramiko

    host = "YOUR_IP_ADDRESS"
    username = "YOUR_LIMITED_USER_ACCOUNT"
    password = "YOUR_PASSWORD"

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command(query)
    x = _stdout.read().decode()
    client.close()
    return x
