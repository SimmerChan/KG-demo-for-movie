# encoding=utf-8

"""

@author: SimmerChan

@contact: hsl7698590@gmail.com

@file: jena_sparql_endpoint.py

@time: 2017/12/20 14:49

@desc:利用SOARQKWrapper向Fuseki发送SPARQL查询，解析返回的结果

"""

from SPARQLWrapper import SPARQLWrapper, JSON
from collections import OrderedDict


class JenaFuseki:
    def __init__(self, endpoint_url='http://localhost:3030/kg_demo_movie/query'):
        self.sparql_conn = SPARQLWrapper(endpoint_url)

    def get_sparql_result(self, query):
        self.sparql_conn.setQuery(query)
        self.sparql_conn.setReturnFormat(JSON)
        return self.sparql_conn.query().convert()

    @staticmethod
    def parse_result(query_result):
        """
        解析返回的结果
        :param query_result:
        :return:
        """
        try:
            query_head = query_result['head']['vars']
            query_results = list()
            for r in query_result['results']['bindings']:
                temp_dict = OrderedDict()
                for h in query_head:
                    temp_dict[h] = r[h]['value']
                query_results.append(temp_dict)
            return query_head, query_results
        except KeyError:
            return None, query_result['boolean']

    def print_result_to_string(self, query_result):
        """
        直接打印结果，用于测试
        :param query_result:
        :return:
        """
        query_head, query_result = self.parse_result(query_result)

        if query_head is None:
            if query_result is True:
                print 'Yes'
            else:
                print 'False'
            print
        else:
            for h in query_head:
                print h, ' '*5,
            print
            for qr in query_result:
                for _, value in qr.iteritems():
                    print value, ' ',
                print

    def get_sparql_result_value(self, query_result):
        """
        用列表存储结果的值
        :param query_result:
        :return:
        """
        query_head, query_result = self.parse_result(query_result)
        if query_head is None:
            return query_result
        else:
            values = list()
            for qr in query_result:
                for _, value in qr.iteritems():
                    values.append(value)
            return values

# TODO 用于测试
if __name__ == '__main__':
    fuseki = JenaFuseki()
    my_query = """
PREFIX : <http://www.kgdemo.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?x WHERE {
?s :personName '周星驰'.?s :hasActedIn ?m.?m :movieTitle ?x
}
limit 1000
    """
    result = fuseki.get_sparql_result(my_query)
    fuseki.print_result_to_string(result)