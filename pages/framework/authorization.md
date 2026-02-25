---
layout: two-cols
layoutClass: gap-4
---

# Authorization Framework

- Users can be members of Service Providers

- Service Provider members can register and submit KPIs for services

- Users can see all service KPI measurements

::right::

<div class="flex flex-col items-center justify-center h-full gap-4">
<div class="w-full">
<AdmonitionType type="important">
Service Providers can register multiple serivces.
</AdmonitionType>
</div>
```mermaid {scale: .9}
flowchart
    subgraph provA["Service Provider A"]
        a(("Alice"))
        s1("Service A")
    end
    subgraph provB["Service Provider B"]
        b(("Bob"))
        s2("Serivce B")
    end
    c(("Charlie"))
    a-->s1
    b-->s2
    b-.->s1
    a-.->s2
    c-.->s1
    c-.->s2
```
</div>