<template lang="">
  <div class="p-4 sm:ml-64 dark:bg-gray-900 min-h-screen bg-gray-200">
    <div
      class="p-4 border-2 border-gray-300 border-dashed rounded-lg dark:border-gray-700 mt-14"
    >
      <div class="inline-flex rounded-md shadow-sm" role="group">
        <AddMember />
        <button
          type="button"
          @click="addMemberModal"
          class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-green-500 border border-gray-900 rounded-l-lg hover:bg-gray-900 hover:text-white focus:z-10 focus:ring-2 focus:ring-gray-500 focus:bg-gray-900 focus:text-white dark:border-white dark:text-white dark:hover:text-white dark:hover:bg-gray-700 dark:focus:bg-gray-700"
        >
          <svg
            class="w-4 h-4 mr-2 fill-current"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 20 18"
          >
            <path
              d="M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z"
            />
          </svg>
          Add New Member
        </button>
        <button
          type="button"
          @click="addBook"
          class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-red-500 border-t border-b border-gray-900 hover:bg-gray-900 hover:text-white focus:z-10 focus:ring-2 focus:ring-gray-500 focus:bg-gray-900 focus:text-white dark:border-white dark:text-white dark:hover:text-white dark:hover:bg-gray-700 dark:focus:bg-gray-700"
        >
          <svg
            class="w-4 h-4 mr-2 fill-current"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 16 20"
          >
            <path
              d="M16 14V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h12a1 1 0 0 0 0-2h-1v-2a2 2 0 0 0 2-2ZM4 2h2v12H4V2Zm8 16H3a1 1 0 0 1 0-2h9v2Z"
            />
          </svg>
          Add New Book
        </button>
       
        <button
          type="button"
          class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-yellow-400 border border-gray-900 rounded-r-md hover:bg-gray-900 hover:text-white focus:z-10 focus:ring-2 focus:ring-gray-500 focus:bg-gray-900 focus:text-white dark:border-white dark:text-white dark:hover:text-white dark:hover:bg-gray-700 dark:focus:bg-gray-700"
        >
          <svg
            class="w-4 h-4 mr-2 fill-current"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 18 20"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M16 1v5h-5M2 19v-5h5m10-4a8 8 0 0 1-14.947 3.97M1 10a8 8 0 0 1 14.947-3.97"
            />
          </svg>
          Return Book
        </button>
      </div>

      <div class="flex flex-row justify-between mt-5">
        <Card
          class="basis-1/4 items-center justify-start h-24 w-64 p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
          title="Books"
          description="69"
        />
        <Card
          class="basis-1/4 items-center justify-start h-24 w-64 p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
          title="Books"
          description="69"
        />
        <Card
          class="basis-1/4 items-center justify-start h-24 w-64 p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
          title="Books"
          description="69"
        />
      </div>

      <div
        class="p-4 bg-white border mt-5 border-gray-200 rounded-lg shadow-sm 2xl:col-span-2 dark:border-gray-700 sm:p-6 dark:bg-gray-800"
      >
        <div class="flex items-center justify-between mb-4 max-w-lg">
          <div class="flex-shrink-0">
            <span
              class="text-xl font-bold leading-none text-gray-900 sm:text-2xl dark:text-white"
              >$45,385</span
            >
            <h3 class="text-base font-light text-gray-500 dark:text-gray-400">
              Sales this week
            </h3>
          </div>
          <div
            class="flex items-center justify-end flex-1 text-base font-medium text-green-500 dark:text-green-400"
          >
            12.5%
            <svg
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </div>
        </div>

        <MainChart />
        <!-- Card Footer -->
        <div
          class="flex items-center justify-between pt-3 mt-4 border-t border-gray-200 sm:pt-6 dark:border-gray-700"
        >
          <div>
            <button
              class="inline-flex items-center p-2 text-sm font-medium text-center text-gray-500 rounded-lg hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
              type="button"
              data-dropdown-toggle="weekly-sales-dropdown"
            >
              Last 7 days
              <svg
                class="w-4 h-4 ml-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                ></path>
              </svg>
            </button>
            <!-- Dropdown menu -->
            <div
              class="z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded shadow dark:bg-gray-700 dark:divide-gray-600"
              id="weekly-sales-dropdown"
            >
              <div class="px-4 py-3" role="none">
                <p
                  class="text-sm font-medium text-gray-900 truncate dark:text-white"
                  role="none"
                >
                  Sep 16, 2021 - Sep 22, 2021
                </p>
              </div>
              <ul class="py-1" role="none">
                <li>
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
                    role="menuitem"
                    >Yesterday</a
                  >
                </li>
                <li>
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
                    role="menuitem"
                    >Today</a
                  >
                </li>
                <li>
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
                    role="menuitem"
                    >Last 7 days</a
                  >
                </li>
                <li>
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
                    role="menuitem"
                    >Last 30 days</a
                  >
                </li>
                <li>
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
                    role="menuitem"
                    >Last 90 days</a
                  >
                </li>
              </ul>
              <div class="py-1" role="none">
                <a
                  href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
                  role="menuitem"
                  >Custom...</a
                >
              </div>
            </div>
          </div>
          <div class="flex-shrink-0">
            <a
              href="#"
              class="inline-flex items-center p-2 text-xs font-medium uppercase rounded-lg text-primary-700 sm:text-sm hover:bg-gray-100 dark:text-primary-500 dark:hover:bg-gray-700"
            >
              Sales Report
              <svg
                class="w-4 h-4 ml-1"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5l7 7-7 7"
                ></path>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Card from "@/components/Card.vue";
import MainChart from "../../components/charts/MainChart.vue";
import AddMember from "../modals/AddMember.vue";
export default {
  components: {
    Card,
    MainChart,
    AddMember
  },
  methods: {
    addMemberModal() {
      document.getElementById('addMember-modal').showModal();
    },
    async addBook() {
      this.$swal("Good job!", "You clicked the button!", "success").then(async () => {
        const steps = ['1', '2', '3']
        const swalQueueStep = this.$swal.mixin({
          confirmButtonText: 'Forward',
          cancelButtonText: 'Back',
          progressSteps: steps,
          input: 'text',
          inputAttributes: {
            required: true
          },
          reverseButtons: true,
          validationMessage: 'This field is required'
        })

        const values = []
        let currentStep

        for (currentStep = 0; currentStep < steps.length;) {
          const result = await swalQueueStep.fire({
            title: `Question ${steps[currentStep]}`,
            inputValue: values[currentStep],
            showCancelButton: currentStep > 0,
            currentProgressStep: currentStep
          })

          if (result.value) {
            values[currentStep] = result.value
            currentStep++
          } else if (result.dismiss === this.$swal.DismissReason.cancel) {
            currentStep--
          } else {
            break
          }
        }

        if (currentStep === steps.length) {
          this.$swal(JSON.stringify(values))
        }
      })
    }
  }
};
</script>
<style lang=""></style>
