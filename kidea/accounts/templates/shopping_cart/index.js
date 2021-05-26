/*
思路：
第一步：獲取所要操作的節點物件
第二步：當頁面載入完後，需要計算本地cookie存了多少【個】商品，把個數賦值給ccount
第三步：為每一個商品對應的新增購物車按鈕繫結一個點選事件onclick
更改本地的cookie
獲取當前商品的pid
迴圈遍歷本地的cookie轉換後的陣列，取出每一個物件的pid進行對比，若相等則該商品不是第一次新增
從購物車中取出該商品，然後更pCount值追加1
否則：建立一個新的物件，儲存到購物中。同時該商品的數量為1
*/
var ccount = document.getElementById("ccount"); //顯示商品總數量的標籤節點物件
var btns = document.querySelectorAll(".list dl dd button"); //所有的購物車按鈕
//約定好用名稱為datas的cookie來存放購物車裡的資料資訊 datas裡所存放的就是一個json字串
var listStr = cookieObj.get("datas");
/*判斷一下本地是否有一個購物車（datas），沒有的話，建立一個空的購物車，有的話就直接拿來使用*/
if(!listStr) { //沒有購物車 datas json
cookieObj.set({
name: "datas",
value: "[]"
});
listStr = cookieObj.get("datas");
}
var listObj = JSON.parse(listStr); //陣列
/*迴圈遍歷陣列，獲取每一個物件中的pCount值相加總和*/
var totalCount = 0; //預設為0
for(var i = 0, len = listObj.length; i < len; i  ) {
totalCount = listObj[i].pCount   totalCount;
}
ccount.innerHTML = totalCount;
/*迴圈為每一個按鈕新增點選事件*/
for(var i = 0, len = btns.length; i < len; i  ) {
btns[i].onclick = function() {
var dl = this.parentNode.parentNode;
var pid = dl.getAttribute("pid");//獲取自定義屬性
var arrs = dl.children;//獲取所有子節點
if(checkObjByPid(pid)) {
listObj = updateObjById(pid, 1)
} else {
var imgSrc = arrs[0].firstElementChild.src;
var pName = arrs[1].innerHTML;
var pDesc = arrs[2].innerHTML;
var price = arrs[3].firstElementChild.innerHTML;
var obj = {
pid: pid,
pImg: imgSrc,
pName: pName,
pDesc: pDesc,
price: price,
pCount: 1
};
listObj.push(obj)
listObj = updateData(listObj);
}
ccount.innerHTML = getTotalCount();
}
}