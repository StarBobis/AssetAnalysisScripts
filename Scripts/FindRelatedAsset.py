import xmltodict


if __name__ == "__main__":
    '''
    Used in large project analysis to locate where our target asset located in.
    This is for solve the problem that a resource will store in different assetbundle files
    instead of all in one single assetbundle, so we need to find them in
    AssetStudio's export list xml file.
    '''

    xml_path = r"C:\Users\Administrator\Desktop\assets.xml"
    new_xml_path = r"C:\Users\Administrator\Desktop\assets_new2.xml"
    search_content = "ch_f_hanhaimomin"

    unique_source_set = set()
    unique_container_set = set()
    # 加载XML文件
    with open(xml_path, "r", encoding="utf-8") as f:
        xml_data = f.read()

    # 解析XML为字典对象
    data_dict = xmltodict.parse(xml_data)

    # 用于存储包含"actor_visual_part"的节点
    actor_assets = []

    # 遍历所有的<Asset>节点
    assets = data_dict['Assets']['Asset']
    for asset in assets:
        container = str(asset['Container'])
        type_id = asset['Type']['@id']
        path_id = asset['PathID']
        source = str(asset['Source'])
        size = asset['Size']

        if container.find(search_content) != -1:
            actor_assets.append(asset)

            # 打印解析结果
            print("Container:", container)
            print("Type ID:", type_id)
            print("Path ID:", path_id)
            print("Source:", source)
            print("Size:", size)
            print("")
            unique_container_set.add(container.split("/")[-2])
            unique_source_set.add(source.split("\\")[-3] + "_" + source.split("\\")[-2])

    # 将包含"actor_visual_part"的节点转换为XML数据
    actor_assets_dict = {'Assets': {'Asset': actor_assets}}
    actor_assets_xml = xmltodict.unparse(actor_assets_dict, pretty=True)

    # 将XML数据写入新的XML文件
    with open(new_xml_path, "w", encoding="utf-8") as f:
        f.write(actor_assets_xml)

    print("---------------------------------------")
    print("---------------------------------------")
    print(unique_source_set)
    print("---------------------------------------")
    print("---------------------------------------")
    print(unique_container_set)

