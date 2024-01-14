// display show ปุ่มกด 2 ปุ่ม แสดงจำนวนลูกค้าที่มา ปุ่มแรกคือ 1-4 ท่าน , ปุ่มที่ 2 คือ 5 ท่านขึ้นไป
// หลังจากกดปุ่มตามจำนวนลูกค้าที่มาแล้ว จะทำการ show/print คิวของลูกค้าออกมา (A or B ตามเงื่อนไข)

function getQueueType(cutomerTotal, queueType) {
    console.log("สวัสดีค่ะ เชิญลูกค้าสู่ร้าน Code class coffee!")
    console.log("วันนี้ลูกค้ามาทั้งหมดกี่ท่านคะ ?")
    */console.log("มาทั้งหมด " + cutomerTotal + " ท่านนะคะ")*/
    console.log("ลูกค้ามาทั้งหมด " + cutomerTotal + " ท่านนะคะ เชิญลูกค้ารับคิว " + queueType);
    console.log("-----------------------------------------------------------")
}


getQueueType("1", "A");
getQueueType("5", "B");

