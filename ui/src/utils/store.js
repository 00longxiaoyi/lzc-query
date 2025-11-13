// store js
//
import { ref } from "vue"
import { pushMessage } from "./toastStore.js"
import { useRequest } from "./useRequest.js"
import { contentWebSocket } from "./webSocketContent.js"


// 固定数据
const softWareTableHeader = ["应用名称", "贡献者"]
const articleTableHeader = ["文章名称", "作者"]
const moneyTableHeader = ["ID", "用户ID", "名称", "作者", "类型", "金额"]

// end

// 数据
const TableData = ref([])
const ContentData = ref("")

// 表单头
const TabelHeaderData = ref([])

// 当前菜单
const MainMenu = ref(null)
const SubMenu = ref(null)

// loading
var IsLoading = ref(false)

// 
const setMainMenu = (value) => {
  MainMenu.value = value
}

const setSubMenu = (value) => {
  SubMenu.value = value
  getData()
}
const getData = async () => {
  const { value: mainMenuValue } = MainMenu.value
  const { value: subMenuValue } = SubMenu.value

  // 应用待审核
  if (subMenuValue == 'noReview') {
    if (mainMenuValue == 'soft') {
      setData(TableData, [], useRequest("/get_soft_ware_pending_data"))
      TabelHeaderData.value = softWareTableHeader
    }

    if (mainMenuValue == 'article') {
      setData(TableData, [], useRequest("/get_article_pending_data"))
      TabelHeaderData.value = articleTableHeader
    }
  }

  const isDownloadingPic = ref(false)
  // 已审核
  if (subMenuValue == 'review') {
    if (mainMenuValue == 'soft') {
      setData(ContentData, "", useRequest("/get_soft_ware_data"))
    }

    if (mainMenuValue == 'article') {
      setData(ContentData, "", useRequest("/get_article_data"))
    }
  }
  // console.log(subMenuValue, mainMenuValue)
  if (subMenuValue == "Summary") {
    setData(ContentData, "", useRequest("/get_soft_article_text_data"))
  }
  if (subMenuValue == 'moeny') {
    setData(TableData, [], useRequest("/get_soft_article_data"))
    TabelHeaderData.value = moneyTableHeader
  }
}
const setData = async (setDataVar, setDataVarDefault, getDataFun) => {
  setDataVar.value = setDataVarDefault
  const getData = getDataFun
  const { error, loading, data, run } = getData
  IsLoading = loading
  await run()
  if (error.value != null) {
    pushMessage(error.value, "error")
    setDataVar.value = setDataVarDefault
  } else {
    pushMessage("数据获取成功", "success")
    setDataVar.value = data.value
  }
}

export {
  MainMenu,
  SubMenu,
  setSubMenu,
  setMainMenu,
  TableData,
  ContentData,
  IsLoading,
  TabelHeaderData
}



