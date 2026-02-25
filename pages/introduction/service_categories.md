---

# Service Categories

<div class="grid grid-cols-2 lg:grid-cols-3 gap-6">
    <div>
        <div  class="card denbi-category">
            Databases
        </div>
        <div v-click="1" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Visits
        </div>
    </div>
    <div>
        <div  class="card denbi-category">
            Tools & Application
        </div>
        <div v-click="1" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Downloads
        </div>
    </div>
    <div>
        <div  class="card denbi-category">
            Support & Consulting
        </div>
        <div v-click="1" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Requests
        </div>
    </div>
    <div>
        <div  class="card denbi-category">
            Libraries & APIs
        </div>
        <div v-click="1" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Downloads
        </div>
    </div>
    <div>
        <div  class="card denbi-category">
            Web Applications
        </div>
        <div v-click="1" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Visits
        </div>
    </div>
    <div>
        <div  class="card denbi-category">
            Workflows & Pipelines
        </div>
        <div v-click="1" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Executions    
        </div>
    </div>
    <div>
        <div v-click="2" class="card nfdi-category">
            Trainings
        </div>
        <div v-click="2" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Participants
        </div>
    </div>
    <div>
        <div v-click="2" class="card nfdi-category">
            Data Curation
        </div>
        <div v-click="2" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Datasets curated
        </div>
    </div>
    <div>
        <div v-click="2" class="card nfdi-category">
            Storage
        </div>
        <div v-click="2" class="mt-2 text-center text-sm text-gray-600">
            <span class="inline-block align-middle mr-1">&#8594;</span>#Storage provided
        </div>
    </div>
</div>

<style>
    .card {
        @apply shadow rounded p-4 text-center border border-gray-200 transition;
        background-color:rgb(240, 240, 240);
    }

    .denbi-category {
        border-width: 1px;
        border-style: solid;
        border-image: linear-gradient(to top right, #00ADEE, gray, #EB008B) 1;
    }

    .nfdi-category {
        border-width: 1px;
        border-style: solid;
        border-image: linear-gradient(to top right, #7AF842, gray, #00F7FB) 1;
    }

</style>