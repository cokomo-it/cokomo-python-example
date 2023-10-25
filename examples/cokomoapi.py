from rich import print
from rich.tree import Tree
from devtools import debug

import cokomo



def visit_neighbours(node, tree=None, root=None):
    """
    Calls the cokomo neighbours API endpoint, which returns a tree strucutre for something
    that is actually a graph. As a consequence, some leave-nodes are the same as the root-node.

    We highlight these repeating root-nodes when calling create_node_label().
    """
    if not tree:
        root = node
        # create tree with root
        tree = Tree(create_node_label(node, highlight=root), guide_style="white")
    for neighbour in node.neighbours:
        if neighbour.relation.direction == "from":
            relation_label = f"[white] ◀︎ {neighbour.relation.type} ◀︎ "
        else:
            relation_label = f"[white] ▶︎ {neighbour.relation.type} ▶︎ "
        child = tree.add(f"relation: {relation_label}")
        child.add(f"title: {create_node_label(neighbour,highlight=root)}")
        child.add(f"id: {neighbour.id}")
        child.add(f"type: {neighbour.type}")
        child.add(f"short_description: {neighbour.short_description}")
        visit_neighbours(neighbour, tree=child, root=root)
    return tree


def create_node_label(node, highlight: cokomo.models.Neighbour):
    if node.id == highlight.id:
        # highlight nodes that are the same as the root node
        format = "[bold bright_yellow]"
    else:
        format = "[bold bright_white]"
    label = f"{format}{node.title} [bright_black]({node.type}) - {node.id}"
    return label


def print_competence_base_details(id: str):
    # configure Cokomo API
    configuration = cokomo.Configuration(
        host="https://cokomo-publicapi.code4you.com"
    )
    # create Cokomo API client using configuration
    with cokomo.ApiClient(configuration) as api_client:
        # get client instance
        api_instance = cokomo.CompetenceBaseApi(api_client)
        try:
            # call Cokomo API
            api_response = api_instance.competence_base_id_neighbours_get(id, depth=2)
            # process response
            print("The response of CompetenceBaseApi->competence_base_id_details_get:\n")
            graph = visit_neighbours(api_response)
            print(graph)
        except cokomo.ApiException as e:
            # handle any errors
            print("Exception when calling CompetenceBaseApi->competence_base_id_details_get: %s\n" % e)