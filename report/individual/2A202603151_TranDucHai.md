# Báo cáo cá nhân — Ngày 2 Object Detection

Đổi tên file theo `MSSV_HoTen.md`, ví dụ `20241234_NguyenVanAn.md`. Điền kết quả thật, xóa dòng hướng dẫn khi nộp. Xem [quy định nộp](../../SUBMISSION.md).

## 1. Thông tin học viên

- Họ tên: Trần Đức Hải
- MSSV: 2A202603151
- Email: dstranhai24@gmail.com
- Lớp: L2A
- Link repo bài làm: https://github.com/HaiiTran/K5-L2-Day02-TranDucHai-2A202603151-ObjectDetection
- Link Colab đã chạy: https://drive.google.com/file/d/1mhNvS-ALYuScaBelC0SJbqxCFSTv111p/view?usp=sharing

## 2. Schema và mini guideline

Dẫn tới [GUIDELINE_MINI.md](../../GUIDELINE_MINI.md). Tóm tắt ba ca mơ hồ đã quyết định, cách áp dụng schema và phần cần giảng viên làm rõ.


## 3. Annotation và self-QC

- Số file nhãn train: 50
- Kết quả checker và lỗi đã xử lý: 
- Danh sách ít nhất 10 ảnh đã rà bằng mắt: 
- Lỗi bỏ sót/box/class phát hiện khi rà và cách sửa: bổ sung box và điều chỉnh viền box
- Commit khóa nhãn ban đầu: 5f36c6260e90387240984dc095d3c7f02d70db44

## 4. Gold QC và rework

| Chỉ số | Trước sửa | Sau sửa nếu có |
|---|---:|---:|
| TP | 452 | 453 |
| FP | 375 | 375 |
| FN | 201 | 200 |
| Precision | 0.5466 | 0.5471 |
| Recall | 0.6922 | 0.6937 |
| F1 | 0.6108 | 0.6117 |
| mean_iou_of_matches | 0.8602 | 0.8603 |
| passed | | false |

Dẫn tới `outputs/annotation_evaluation.json` trong repo. Nếu rework, ghi ảnh, lỗi đã kiểm, quyết định sửa/giữ và lý do. Không suy nguyên nhân chỉ từ FP/FN. Không có rework thì ghi rõ.

## 5. Kết quả YOLO

- Runtime, GPU/CPU, phiên bản Ultralytics và Torch: Tesla T4; Ultralytics 8.4.208; PyTorch 2.14.1+cu130
- Các tham số thay đổi so với notebook nếu có và lý do:
- Đường dẫn best checkpoint trong phiên chạy:

| Chỉ số trên 10 ảnh eval | Giá trị |
|---|---:|
| Precision | 0.3269901429870196 |
| Recall | 0.36391843971631205 |
| mAP50 | 0.3520424271222671 |
| mAP50–95 | 0.23337096221955367 |

Đặt cả 2 folder `assets/eval_predictions/` và `assets/yolo26_runs/` (giải nén từ `day2_colab_outputs.zip`) cạnh báo cáo và dẫn link tương đối. Không chỉ ghi số; chỉ ra ít nhất một ảnh và vật thể cụ thể.

Trả lời bốn câu hỏi cuối notebook:

1. Lớp nào recall thấp nhất? Ảnh nào minh họa?
- lớp `truck1` có recall thấp nhất= 0. Ảnh `drive_058.jpg` có chứa `truck` nhưng mô hình hầu như chỉ dự đoán ra `car`.
2. Nếu mAP50 cao nhưng mAP50–95 thấp, cần kiểm điều gì trên box? 
- Điều này chứng tỏ mô hình xác định đúng vị trí bao quát của vật thể, nhưng bounding box lệch, không khớp với vật thể thực tế. Cần kiểm tra  gán nhãn có bị rộng quá, hẹp quá, hoặc bị lệch so với biên thực tế của xe hay không.
3. Lỗi class nào có thể liên quan guideline? Dữ kiện nào hỗ trợ nhận xét?
-  Lỗi gán nhãn không rõ ràng hoặc không nhất quán. Dữ kiện như Prediction và Ground Truth có thể dùng để nhận xét.
4. Vì sao không dùng 10 ảnh eval để train? Vai trò validation của chúng trong notebook là gì?
-  Nếu dùng 10 ảnh eval để train, mô hình sẽ học trực tiếp trên các ảnh này và kết quả sẽ bị overfitting. 
- 10 ảnh eval này đóng vai trò làm thước đo khách quan độc lập để theo dõi tiến trình học qua từng epoch và là tiêu chuẩn duy nhất để lựa chọn checkpoint tốt nhất.

## 6. Khó khăn và cách xử lý

| Bước/thời điểm | Lỗi quan sát | Cách đã thử | Kết quả/còn thiếu |
|---|---|---|---|
| | | | |

## 7. Tự đánh giá theo rubric

Đối chiếu [RUBRIC.md](../../RUBRIC.md): phần nào đã có kết quả, phần nào còn thiếu hoặc chưa kiểm được. Không tự nhận hoàn thành bước chưa chạy.
- Phần đã có kết quả: Hoàn thành và định dạng YOLO, Độ bám sát và hình học box, Phân lớp nhất quán, Mini guideline và quyết định mơ hồ, Pipeline YOLO và phân tích.

## 8. Công cụ AI và tài liệu tham khảo

Ghi công cụ đã dùng, dùng ở bước nào và phần đã tự kiểm tra; không dùng thì ghi rõ. Liệt kê nguồn ngoài repo được sử dụng. Không ghi mật khẩu/token hoặc đính kèm gold train.
- không dùng công cụ
