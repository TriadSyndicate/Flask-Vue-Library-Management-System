<template lang="">
    <div>
        <div id="mainChart"></div>
    </div>
</template>
<script>
import ApexCharts from 'apexcharts'
var options = {
    theme: {
        mode: 'dark',
        palette: 'palette1',
        monochrome: {
            enabled: false,
            color: '#255aee',
            shadeTo: 'light',
            shadeIntensity: 0.65
        },
    },
    chart: {
        id: 'apexchart-main',
        height: 380,
        type: 'area',
        stacked: false,
    },
    stroke: {
        curve: 'straight'
    },
    series: [{
        name: "Music",
        data: [11, 15, 26, 20, 33, 27]
    },
    {
        name: "Photos",
        data: [32, 33, 21, 42, 19, 32]
    },
    {
        name: "Files",
        data: [20, 39, 52, 11, 29, 43]
    }
    ],
    xaxis: {
        categories: ['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2'],
    },
    tooltip: {
        followCursor: true
    },
    fill: {
        opacity: 1,
    },

}
export default {
    data() {
        return {
            darkMode: localStorage.getItem('color-theme'),
        }
    },
    methods: {
        renderChart() {
            var chart = new ApexCharts(document.querySelector("#mainChart"), options);
            chart.render();
        },
        updateFromLocalStorage() {
            this.darkMode = localStorage.getItem('color-theme')
        }
    },
    mounted() {
        this.renderChart()
        setInterval(() => {
            this.updateFromLocalStorage()
        }, 50);
    },
    computed: {
        theme() {
            if(this.darkMode == 'dark') {
                return '#192734'
            } else {
                return '#fff'
            }
        }
    },
    watch: {
        darkMode(newVal, oldVal) {
            console.log(`Watch dark mode is ${newVal} and Old Val is ${oldVal}`)
            ApexCharts.exec('apexchart-main','updateOptions', {
                theme: {
                    mode: `${newVal}`,
                    palette: 'palette2',
                },
                chart:{
                    background: this.theme,
                }
            }, false, false, false)
        }
    }
}
</script>
<style lang="">
    
</style>