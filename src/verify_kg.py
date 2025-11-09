# verify_kg.py
from py2neo import Graph

def verify_knowledge_graph():
    """验证知识图谱导入完整性"""
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "WH123456"))
    
    
    # 检查各类型节点数量
    queries = {
        "疾病节点": "MATCH (d:Disease) RETURN count(d) as count",
        "症状节点": "MATCH (s:Symptom) RETURN count(s) as count",
        "药品节点": "MATCH (d:Drug) RETURN count(d) as count",
        "食物节点": "MATCH (f:Food) RETURN count(f) as count",
        "检查项目": "MATCH (c:Check) RETURN count(c) as count",
        "生产商": "MATCH (p:Producer) RETURN count(p) as count",
        "科室": "MATCH (d:Department) RETURN count(d) as count",
        "总关系数": "MATCH ()-[r]-() RETURN count(r) as count"
    }
    
    for label, query in queries.items():
        result = graph.run(query).data()
        count = result[0]['count'] if result else 0
        print(f"{label}: {count}")
    
    # 验证具体关系
    print("\n=== 关系验证 ===")
    relation_queries = {
        "疾病-症状关系": "MATCH (d:Disease)-[:has_symptom]->(s:Symptom) RETURN count(*) as count",
        "疾病-药品关系": "MATCH (d:Disease)-[:recommand_drug]->(dru:Drug) RETURN count(*) as count",
        "疾病-食物关系": "MATCH (d:Disease)-[:recommand_eat]->(f:Food) RETURN count(*) as count"
    }
    
    for label, query in relation_queries.items():
        result = graph.run(query).data()
        count = result[0]['count'] if result else 0
        print(f"{label}: {count}")

if __name__ == "__main__":
    verify_knowledge_graph()