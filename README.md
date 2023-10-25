## Install requirements
```shell
$ pip install pipenv
```

## Run example

```shell
$ pipenv run python -m examples.show_neighbours 5f052fd6-e566-4ade-9497-e3c97606936d
```

## Output
```
The response of CompetenceBaseApi->competence_base_id_details_get:

Natürliche Zahl (Concept) - 5f052fd6-e566-4ade-9497-e3c97606936d
├── relation:  ◀︎ to be set ◀︎ 
│   ├── title: ℕ - natürliche Zahlen (Principle) - 53a1d7f2-63a1-40a3-a44f-48f163400a35
│   ├── id: 53a1d7f2-63a1-40a3-a44f-48f163400a35
│   ├── type: Principle
│   ├── short_description: 
│   ├── relation:  ◀︎ is composed of ◀︎ 
│   │   ├── title: Zahlenmengen (Principle) - 2625d7cb-1468-442a-b746-40dadca95d6c
│   │   ├── id: 2625d7cb-1468-442a-b746-40dadca95d6c
│   │   ├── type: Principle
│   │   └── short_description: 
│   ├── relation:  ◀︎ specializes ◀︎ 
│   │   ├── title: ℕ \ {0} (Principle) - b2b6650f-6123-4dcd-ba0e-65a8d9515dbb
│   │   ├── id: b2b6650f-6123-4dcd-ba0e-65a8d9515dbb
│   │   ├── type: Principle
│   │   └── short_description: Menge der natürlichen Zahlen ohne Null
│   ├── relation:  ▶︎ specializes ▶︎ 
│   │   ├── title: ℤ - ganze Zahlen (Principle) - 48c22506-f0c3-42ac-8e39-0cecd8158096
│   │   ├── id: 48c22506-f0c3-42ac-8e39-0cecd8158096
│   │   ├── type: Principle
│   │   └── short_description: 
│   └── relation:  ▶︎ to be set ▶︎ 
│       ├── title: Natürliche Zahl (Concept) - 5f052fd6-e566-4ade-9497-e3c97606936d
│       ├── id: 5f052fd6-e566-4ade-9497-e3c97606936d
│       ├── type: Concept
│       └── short_description: Die natürlichen Zahlen umfassen diejenigen Zahlen, die beim Zählvorgang verwendet werden, In 
│           einigen Definitionen wird auch die 0 (Null) zu den natürlichen Zahlen hinzugezählt.
└── relation:  ◀︎ specializes ◀︎ 
    ├── title: Anzahl (Concept) - 78a90cd8-bf07-4c72-84a8-7ccdaf1c9ff5
    ├── id: 78a90cd8-bf07-4c72-84a8-7ccdaf1c9ff5
    ├── type: Concept
    ├── short_description: Die Anzahl ist ein Rechenwert, der besagt aus wie vielen Objekten eine Menge besteht. Die Anzahl kann 
    │   durch das Zählen der Menge bestimmt werden.
    └── relation:  ▶︎ specializes ▶︎ 
        ├── title: Natürliche Zahl (Concept) - 5f052fd6-e566-4ade-9497-e3c97606936d
        ├── id: 5f052fd6-e566-4ade-9497-e3c97606936d
        ├── type: Concept
        └── short_description: Die natürlichen Zahlen umfassen diejenigen Zahlen, die beim Zählvorgang verwendet werden, In 
            einigen Definitionen wird auch die 0 (Null) zu den natürlichen Zahlen hinzugezählt.



```
