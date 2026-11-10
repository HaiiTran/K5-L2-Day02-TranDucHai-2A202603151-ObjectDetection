# Mini guideline — bài làm cá nhân

> Điền nội dung này trước khi bắt đầu gán nhãn. Giữ lại các quyết định sau khi self-QC.

## Định nghĩa lớp

| Lớp | Định nghĩa của bạn | Ví dụ/điểm phân biệt |
| --- | --- | --- |
| `car` | Xe ô tô con, phương tiện cá nhân hoặc thương mại nhỏ phục vụ chở người/hàng nhẹ (4–7 chỗ: sedan, hatchback, SUV, taxi). | - Xe có từ 4–7 chỗ ngồi, cửa sổ hai bên xe, khoang hành khách và cốp/thùng phân chia rõ ràng.<br>- Xe bán tải có thùng sau vẫn thuộc lớp `car`.
| `truck` | Xe tải chở hàng hóa/vật liệu hạng trung đến nặng, xe đầu kéo. | - Xe có thùng hàng/khoang chở vật liệu riêng biệt tách rời với cabin lái, xe ben, xe bồn.<br>- Xe tải van thùng kín liền khối thuộc (`van`). |
| `bus` | Xe kinh doanh vận tải hành khách sử dụng xe ô tô chở người từ 08 chỗ trở lên không kể chỗ của người lái xe| - Thân xe to lớn, dài, có nhiều hàng cửa kính dọc hai bên hông xe, phục vụ chở nhiều người (xe buýt đô thị, xe khách liên tỉnh, minibus chở khách lớn).|
| `van` | Xe tải van, minivan có thân hộp vuông dạng liền một khối dùng chở hàng nhẹ hoặc chở nhóm người. | - Xe có thiết kế thân liền khối, trần xe cao và vuông vức từ trước ra sau. |

## Quy tắc chung

- Box bám sát vật thể nghĩa là: box ôm khít các mép ngoài cùng của phần thân xe thực tế nhìn thấy được; không lấy thừa mặt đường, vỉa hè, bầu trời hay lấn sang xe bên cạnh; không lấy hàng hóa chở trên xe.
- Vật thể bị che khuất: Vật thể bị che một phần vẫn gán box quanh phần nhìn thấy được nếu nhận diện được lớp.
- Vật thể bị cắt bởi rìa ảnh: Cạnh của box chạm đúng mép biên ảnh tại vị trí bị cắt.
- Vật thể rất nhỏ/mơ hồ: Nếu vật thể quá nhỏ hoặc quá mờ ở xa không  có đặc trưng nhận diện thì bỏ qua.

## Ghi lại quyết định cho ít nhất ba ca mơ hồ

| Ảnh | Tình huống | Quyết định cuối | Lý do theo schema |
| --- | --- | --- | --- |
| `drive_040` | vật thể ở xa và bị che khuất, bị mờ, không rõ hình ảnh | không thực hiện label | không nhận diện được vật thể |
| `drive_005` | quá nhiều vật thể chèn hình nên nhau| không thực hiện label | không nhận diện được vật thể |
| `drive_020` | có những chiếc xe bị chận bởi biển quảng cáo, cây cối | không thực hiện label | không nhận diện được vật thể |
