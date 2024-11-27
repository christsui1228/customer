<template>
    <n-card>
      <n-space vertical>
        <n-space>
          <n-input
            v-model:value="filters.customerName"
            placeholder="搜索客户"
            clearable
            @clear="handleClearFilter('customerName')"
          >
            <template #prefix>
              <n-icon><Search /></n-icon>
            </template>
          </n-input>
        </n-space>
        <n-data-table
          :loading="mockCustomerStore.loading"
          :columns="columns"
          :data="filteredCustomers"
          :pagination="pagination"
          @update:value="handleUpdateValue"
        />
      </n-space>
    </n-card>
  </template>
  
  <script setup lang="ts">
  import { ref, reactive, h, computed } from 'vue'
  import {
    NCard,
    NButton,
    NDataTable,
    NInput,
    NSpace,
    NIcon,
    NSelect,
    NDatePicker,
    useMessage
  } from 'naive-ui'
  import { TrashOutline, Search } from '@vicons/ionicons5'
  
  const message = useMessage()
  
  // 筛选条件
  const filters = reactive({
    customerName: '',
  })
  
  // 客户类型选项
  const customerTypes = [
    { label: '普通客户', value: 'normal' },
    { label: 'VIP客户', value: 'vip' },
  ]
  
  // 模拟数据
  const mockCustomerStore = reactive({
    loading: false,
    customers: [
      {
        id: 1,
        store: '北京店',
        customerId: 'CUS001', 
        customerType: 'normal',
        requirement: '常规需求',
        description: '测试描述',
        expectedOrderTime: '2024-01-20',
        expectedAmount: 1000,
        lastModified: '2024-01-19',
        createDate: '2024-01-18'
      }
    ]
  })
  
  // 创建一个空行
  const createEmptyRow = () => {
    return {
      id: Date.now() + Math.random(),
      store: '',
      customerId: '',
      customerType: '',
      requirement: '',
      description: '',
      expectedOrderTime: null,
      expectedAmount: null,
      lastModified: '',
      createDate: '',
      isEmpty: true
    }
  }
  
  // 确保始终有两个空行
  const ensureEmptyRows = () => {
    let emptyRowCount = 0
    for (let i = mockCustomerStore.customers.length - 1; i >= 0; i--) {
      if (!mockCustomerStore.customers[i].customerId) {
        emptyRowCount++
      } else {
        break
      }
    }
    
    if (emptyRowCount < 2) {
      const rowsToAdd = 2 - emptyRowCount
      for (let i = 0; i < rowsToAdd; i++) {
        mockCustomerStore.customers.push(createEmptyRow())
      }
    } else if (emptyRowCount > 2) {
      mockCustomerStore.customers.splice(
        mockCustomerStore.customers.length - (emptyRowCount - 2),
        emptyRowCount - 2
      )
    }
  }
  
  // 初始添加两个空行
  mockCustomerStore.customers.push(createEmptyRow())
  mockCustomerStore.customers.push(createEmptyRow())
  
  // 过滤后的数据
  const filteredCustomers = computed(() => {
    return mockCustomerStore.customers.filter(customer => {
      const nameMatch = !filters.customerName || 
        customer.customerId.toLowerCase().includes(filters.customerName.toLowerCase())
      return nameMatch
    })
  })
  
  // 清除筛选条件
  const handleClearFilter = (field: string) => {
    filters[field as keyof typeof filters] = ''
  }
  
  // 分页配置
  const pagination = reactive({
    page: 1,
    pageSize: 10,
    showSizePicker: true,
    pageSizes: [10, 20, 30, 40]
  })
  
  // 表格列定义
  const columns = [
    {
      title: '店铺',
      key: 'store',
      render: (row: any) => {
        return h(NInput, {
          value: row.store,
          placeholder: '请输入店铺',
          onUpdateValue: (v) => {
            row.store = v
            if (v) row.isEmpty = false
            ensureEmptyRows()
          }
        })
      }
    },
    {
      title: '客户ID',
      key: 'customerId',
      render: (row: any) => {
        return h(NInput, {
          value: row.customerId,
          placeholder: '请输入客户ID',
          onUpdateValue: (v) => {
            row.customerId = v
            if (v) row.isEmpty = false
            ensureEmptyRows()
          }
        })
      }
    },
    {
      title: '客户类型',
      key: 'customerType',
      render: (row: any) => {
        return h(NSelect, {
          value: row.customerType,
          options: customerTypes,
          placeholder: '请选择类型',
          onUpdateValue: (v) => {
            row.customerType = v
            if (v) row.isEmpty = false
            ensureEmptyRows()
          }
        })
      }
    },
    {
      title: '客户需求',
      key: 'requirement',
      render: (row: any) => {
        return h(NInput, {
          value: row.requirement,
          placeholder: '请输入需求',
          onUpdateValue: (v) => {
            row.requirement = v
            if (v) row.isEmpty = false
            ensureEmptyRows()
          }
        })
      }
    },
    {
      title: '情况描述',
      key: 'description',
      render: (row: any) => {
        return h(NInput, {
          value: row.description,
          placeholder: '请输入描述',
          onUpdateValue: (v) => {
            row.description = v
            if (v) row.isEmpty = false
            ensureEmptyRows()
          }
        })
      }
    },
    {
      title: '预计下单时间',
      key: 'expectedOrderTime',
      render: (row: any) => {
        return h(NDatePicker, {
          value: row.expectedOrderTime,
          type: 'date',
          clearable: true,
          onUpdateValue: (v) => {
            row.expectedOrderTime = v
            if (v) row.isEmpty = false
            ensureEmptyRows()
          }
        })
      }
    },
    {
      title: '预计下单金额',
      key: 'expectedAmount',
      render: (row: any) => {
        return h(NInput, {
          value: row.expectedAmount,
          placeholder: '请输入金额',
          onUpdateValue: (v) => {
            row.expectedAmount = v
            if (v) row.isEmpty = false
            ensureEmptyRows()
          }
        })
      }
    },
    {
      title: '最新修改日期',
      key: 'lastModified',
      render: (row: any) => {
        return row.lastModified || '—'
      }
    },
    {
      title: '创建日期',
      key: 'createDate',
      render: (row: any) => {
        return row.createDate || '—'
      }
    },
    {
      title: '操作',
      key: 'actions',
      render: (row: any) => {
        if (!row.isEmpty) {
          return h(
            NButton,
            {
              size: 'small',
              type: 'error',
              onClick: () => handleDelete(row)
            },
            { 
              icon: () => h(NIcon, null, { default: () => h(TrashOutline) }),
              default: () => '删除'
            }
          )
        }
        return null
      }
    }
  ]
  
  // 处理删除
  const handleDelete = (row: any) => {
    const index = mockCustomerStore.customers.findIndex(item => item.id === row.id)
    if (index !== -1) {
      mockCustomerStore.customers.splice(index, 1)
      ensureEmptyRows()
      message.success('删除成功')
    }
  }
  
  // 处理数据更新
  const handleUpdateValue = (customers: any[]) => {
    mockCustomerStore.customers = customers
    ensureEmptyRows()
  }
  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  </style>