# Mini guideline — bài làm cá nhân

> Điền nội dung này trước khi bắt đầu gán nhãn. Giữ lại các quyết định sau khi self-QC.

## Định nghĩa lớp

| Lớp | Định nghĩa của bạn | Ví dụ/điểm phân biệt |
| --- | --- | --- |
| `car` | Xe ô tô con, phương tiện cá nhân hoặc thương mại nhỏ phục vụ chở người/hàng nhẹ (4–7 chỗ: sedan, hatchback, SUV, taxi) và xe bán tải cabin nhỏ. | - Xe có từ 4–7 chỗ ngồi, cửa sổ hai bên xe, khoang hành khách và cốp/thùng phân chia rõ ràng.<br>- **Điểm phân biệt:** Xe bán tải (pickup truck) có thùng sau vẫn thuộc lớp `car` (không gán vào `truck`).
| `truck` | Xe tải chở hàng hóa/vật liệu hạng trung đến nặng, xe đầu kéo. | - Xe có thùng hàng/khoang chở vật liệu riêng biệt tách rời với cabin lái, xe ben, xe bồn.<br>- **Điểm phân biệt:** Không gán xe bán tải cabin nhỏ (thuộc `car`) và xe tải van thùng kín liền khối (`van`). |
| `bus` | Xe kinh doanh vận tải hành khách sử dụng xe ô tô chở người từ 08 chỗ trở lên không kể chỗ của người lái xe| - Thân xe to lớn, dài, có nhiều hàng cửa kính dọc hai bên hông xe, phục vụ chở nhiều người (xe buýt đô thị, xe khách liên tỉnh, minibus chở khách lớn).<br>- **Điểm phân biệt:** Phân biệt với xe van chở người/minivan 7–16 chỗ cỡ nhỏ thuộc `van`. |
| `van` | Xe tải van, minivan có thiết kế dạng thân hộp vuông vức liền một khối dùng chở hàng nhẹ hoặc chở nhóm người. | - Xe có thiết kế thân liền khối (thùng chở hàng và khoang lái nối liền), trần xe cao và vuông vức từ trước ra sau.<br>- **Điểm phân biệt:** Khác với `car` (thân xe liền khối cao, không phân khoang cốp) và khác với `bus` (kích thước nhỏ hơn xe khách/xe buýt lớn). |

## Quy tắc chung

- Box bám sát vật thể nghĩa là: Bounding box phải ôm khít các mép ngoài cùng của phần thân xe thực tế nhìn thấy được; không lấy thừa mặt đường, vỉa hè, bầu trời hay lấn sang xe bên cạnh; không lấy hàng hóa chở trên xe.
- Vật thể bị che khuất: Nếu vật thể bị che quá 80% thì bỏ qua, nếu không vẽ box bao quanh toàn bộ phần diện tích nhìn thấy được của xe miễn là đủ đặc trưng nhận diện đúng lớp. Phần bị cắt thì vẽ ước lượng và không cắt quá nhiều vào xe bên cạnh (nếu có).
- Vật thể bị cắt bởi rìa ảnh: Cạnh của box chạm đúng mép biên ảnh tại vị trí bị cắt. Vật thể bị cắt quá 80% thì bỏ qua.
- Vật thể rất nhỏ/mơ hồ: Nếu vật thể quá nhỏ hoặc quá mờ ở xa không  có đặc trưng nhận diện thì bỏ qua.

## Ghi lại quyết định cho ít nhất ba ca mơ hồ

| Ảnh | Tình huống | Quyết định cuối | Lý do theo schema |
| --- | --- | --- | --- |
| `drive_040` | vật thể ở xa và bị che khuất, bị mờ, không rõ hình ảnh | bỏ qua | không nhìn rõ vật thể |
| `drive_...` | | | |
| `drive_...` | | | |
