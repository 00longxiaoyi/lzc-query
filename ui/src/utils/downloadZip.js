import { getTodayLocal } from "./util"
import { saveAs } from "file-saver"

export default async function downloadZip() {
  const response = await fetch("/api/download/zipfile")
  if (!response.ok) {
    return "下载失败"
  }

  const blob = await response.blob()
  saveAs(blob, `${getTodayLocal()}.zip`)
}
