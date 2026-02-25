---

# Scorpion Architecture

<div class="flex flex-row">
<div>
```mermaid {scale: .5}
architecture-beta
    group scorpion(cloud)[Scorpion]
    group provA(internet)[Service Provider A]
    group provB(internet)[Service Provider B]
    service gui(server)[Web Interface] in scorpion
    service api(server)[API] in scorpion
    service metaDB(database)[Metadata] in scorpion
    service timeDB(database)[Results] in scorpion
    service spreadsheet(disk)[Spreadsheet] in provA
    service service1(database)[Service 1] in provA
    service matomo(server)[Matomo] in provB
    service service2(server)[Service 2] in provB
    service service3(database)[Service 3] in provB
    api:B -- T:timeDB
    api:L -- R:metaDB
    gui:L -- R:api
    spreadsheet{group}:L --> R:gui
    service1:L -- R:spreadsheet  
    matomo:B --> T:api
    service2:L -- R:matomo
    service3:R -- L:matomo
```
</div>

<v-clicks>

- Heterogeneous service provider landscape

- Some use monitoring service (e.g. Matomo), others "count mails in a spreadsheet"

- Solution required to make this diverse reporting available to <span v-mark="{ at: 3, color: '#5a7bbe', type: 'circle' }">project management teams</span>

</v-clicks>
</div>