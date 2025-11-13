import { pushMessage } from "./toastStore.js"

export function contentWebSocket(successMes, lastMes) {
  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  var host = window.location.host; // 当前域名 + 端口

  // 开发环境
  if (host.includes("127.0.0.1") || host.includes("localhost")) {
    host = "127.0.0.1:8080"; // 开发环境使用本地端口
  }

  const webSocketUrl = `${protocol}://${host}/ws/pics_info`

  const ws = new WebSocket(webSocketUrl)
  ws.onmessage = (event) => {
    var data = JSON.parse(event.data)
    pushMessage(data.data, data.type, data.type == "success" ? 3000 : 5000)
    successMes && successMes()
    // warning 标识为最后一条消息
    if (data.type == "warning") {
      lastMes && lastMes()
      ws.close(1000, "用户主动关闭连接");
    }
  };
}



