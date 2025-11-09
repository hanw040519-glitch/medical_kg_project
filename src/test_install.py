
from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "WH123456"))

def test_neo4j_operations():
    """测试Neo4j的增删改查基本操作"""
    
    # 1. 增
    graph.run("CREATE (p:Person {name: '张三', age: 30})")
    graph.run("CREATE (p:Person {name: '李四', age: 25})")
    print("创建测试数据完成")
    
    # 2. 查
    print("\n查询所有人员")
    result = graph.run("MATCH (p:Person) RETURN p.name, p.age")
    for record in result:
        print(f"姓名: {record['p.name']}, 年龄: {record['p.age']}")
    
    # 3. 改
    print("\n更新数据")
    graph.run("MATCH (p:Person {name: '张三'}) SET p.age = 31")
    result = graph.run("MATCH (p:Person {name: '张三'}) RETURN p.age")
    print(f"张三的新年龄: {result.data()[0]['p.age']}")
    
    # 4. 删
    graph.run("MATCH (p:Person) DELETE p")
    print("数据删除完成")

if __name__ == "__main__":
    test_neo4j_operations()