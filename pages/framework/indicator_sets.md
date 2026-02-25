---
layout: two-cols
layoutClass: gap-4
---

# KPI Necessities
<div class="flex flex-row gap-2">
    <div class="card denbi-category h-fit">
        <span class="font-semibold text-lg">Databases</span>
    </div>
    <div class="card h-fit w-1/2">
        <div class="flex flex-col gap-0">
            <span class="flex justify-left font-bold text-sm">Mandatory</span>
            <p class="flex flex-col text-gray-500 text-xs">
            <span class="flex justify-left">&#8594; #Visits</span>
            </p>
        </div>
        <div class="flex flex-col gap-0">
            <span class="flex justify-left font-bold text-sm">Recommended</span>
            <p class="flex flex-col text-gray-500 text-xs">
            <span class="flex justify-left">&#8594; #Recurring Users</span>
            <span class="flex justify-left">&#8594; #Support Tickets</span>
            <span class="flex justify-left">&#8594; #Unique Users</span>
            </p>
        </div>
        <div class="flex flex-col gap-0">
            <span class="flex justify-left font-bold text-sm">Optional</span>
            <p class="flex flex-col text-gray-500 text-xs">
            <span class="flex justify-left">&#8594; #Citations</span>
            <span class="flex justify-left">&#8594; #Downloads</span>
            <span class="flex justify-left">&#8594; #Hits</span>
            <span class="flex justify-left">&#8594; #Publications</span>
            </p>
        </div>
    </div>
</div>


<style>
    .card {
        @apply shadow p-4 text-center border border-gray-500 transition;
        background-color:rgb(240, 240, 240);
    }
    .denbi-category {
        border-width: 1px;
        border-style: solid;
        border-image: linear-gradient(to top right, #00ADEE, gray, #EB008B) 1;
    }
</style>

::right::

<br>
<br>

- **Mandatory KPI**
    - Indicators required by DFG

- **Recommended KPI**
    - Indicators relevant to most services of this category

- **Optional KPI**
    - Indicators useful to understand the impact of a service

---
layout: two-cols
layoutClass: gap-4
---

# KPI Set Definition

````md magic-move
```json
{
    "mandatory": [
        "Visits"
    ],
    "recommended": [
        "Recurring Users",
        "Support Tickets",
        "Unique Users"
    ],
    "optional": [
        "Citations",
        "Downloads",
        "Hits",
        "Publications"
    ]
}
```
```json
{
    "mandatory": [
        "Visits"
    ],
    "recommended": [
        "Recurring Users",
        "Support Tickets",
        "Unique Users"
    ],
    "optional": [
        "Citations",
        "Downloads",
        "Hits",
        "Publications",
        "Storage Usage"
    ]
}
```
````

::right::

<br>
<br>

```mermaid {theme: 'default', scale: .75}
---
config:
  sankey:
    showValues: false
---
sankey-beta
    Databases,Visits,1
    Databases,Citations,1
    Databases,Unique Users,1
    Databases,Recurring Users,1
    Databases,Support Tickets,1
    Databases,Publications,1
    Databases,Downloads,1
    Databases,Hits,1
    Web Applications,Citations,1
    Web Applications,Unique Users,1
    Web Applications,Visits,1
    Web Applications,Visits Duration,1
    Web Applications,Pageviews,1
    Web Applications,Actions,1
    Web Applications,Actions Per Visit,1
    Web Applications,Support Tickets,1
    Web Applications,Registered Users,1
    Tools & Applications,Downloads,1
    Tools & Applications,Citations,1
    Tools & Applications,Support Tickets,1
    Tools & Applications,Download Distinct IPs,1
    Tools & Applications,Unique Users,1
    Tools & Applications,Executions,1
    Support & Consulting,Support Tickets,1
    Support & Consulting,Publications,1
    Support & Consulting,Citations,1
    Workflows & Pipelines,Citations,1
    Workflows & Pipelines,Executions,1
    Workflows & Pipelines,Unique Users,1
    Workflows & Pipelines,Projects,1
    Workflows & Pipelines,Storage Usage,1
    Libraries & APIs,Downloads,1
    Libraries & APIs,Citations,1
    Libraries & APIs,Suppor Tickets,1
    Libraries & APIs,Publications,1
    Libraries & APIs,Grant Applications,1
```