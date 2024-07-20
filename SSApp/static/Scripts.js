function setDefult_Modal() {
    modal[0].innerHTML = `
    <p> <strong>Người phát hiện: </strong> ... </p>
    <p> <strong>Tên nguyên tố: </strong> ... </p>
    <p> <strong>Kí hiệu: </strong> ... </p>
    <p> <strong>Thể: </strong> ... </p>
    <p> <strong>Số hiệu nguyên tử: </strong> ... </p>
    <p> <strong>Nguyên tử khối: </strong> ... </p>
    <p> <strong>Phân lớp: </strong> ... </p>
    <p> <strong>Nhóm: </strong> ... </p>
    <p> <strong>Chu kì: </strong> ... </p>
    <p> <strong>Phân loại: </strong> ... </p>
    <p> <strong>Khối lượng riêng: </strong> ... </p>
    <p> <strong>Nhiệt độ sôi: </strong> ...</p>
    <p> <strong>Nhiệt độ nóng chảy: </strong> ...</p>
    <p> <strong>Độ âm điện: </strong> ...</p>
    <p> <strong>Số oxi hóa: </strong> ...</p>
    <p> <strong>Cấu hình (e): </strong> ... </p>
    <p> <strong>Mô tả hình dạng xuất hiện: </strong> ...</p>
    <img src="{%static 'Image/logo/og-image.jpg' %}" alt="" style="width: 100%">
    `
}

function getElement_Info(element) {
    const modal = document.getElementsByClassName("modal-body")
    console.log(`/api/chemical/?element=${element}`);
    fetch(`/api/chemical?element=${element}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);

            var electronegativity = data.electronegativity ? data.electronegativity : "Không có"
            var oxidation = data.oxidation ? data.oxidation : "Không có"
            var appearance = data.appearance ? data.appearance : "N/A"
            var boil_K = data.boil_K ? data.boil_K : "Không có"
            var melt_K = data.melt_K ? data.melt_K : "Không có"

            string = `
            <p> <strong>Người phát hiện: </strong> ${data.discoverer} </p>
            <p> <strong>Tên nguyên tố: </strong> ${data.name_of_chemical} </p>
            <p> <strong>Kí hiệu: </strong> ${data.symbol_chemical} </p>
            <p> <strong>Thể: </strong> ${data.plase} </p>
            <p> <strong>Số hiệu nguyên tử: </strong> ${data.id} </p>
            <p> <strong>Nguyên tử khối: </strong> ${data.atomic_mass.toFixed(3)} </p>
            <p> <strong>Phân lớp: </strong> ${data.block} </p>
            <p> <strong>Nhóm: </strong> ${data.group} </p>
            <p> <strong>Chu kì: </strong> ${data.period} </p>
            <p> <strong>Phân loại: </strong> ${data.classify} </p>
            <p> <strong>Khối lượng riêng: </strong> ${data.density} </p>
            <p> <strong>Nhiệt độ sôi: </strong> ${boil_K} </p>
            <p> <strong>Nhiệt độ nóng chảy: </strong> ${melt_K} </p>
            <p> <strong>Độ âm điện: </strong> ${electronegativity} </p>
            <p> <strong>Số oxi hóa: </strong> ${oxidation} </p>
            <p> <strong>Cấu hình (e): </strong> ${data.configuration} </p>
            <p> <strong>Mô tả hình dạng xuất hiện: </strong> ${appearance} </p>
            <p> <strong> => </strong> ${data.summary} </p>
            <img src="${data.image_URL}" alt="Hình ảnh của ${data.name_of_chemical}" style="width: 100%">
            `
            modal[0].innerHTML = string
            console.log(string);
        })
}

