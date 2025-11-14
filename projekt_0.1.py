import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


def create_metric_widget(title, value):
   # Создает виджет метрики
    widget = QGroupBox(title)
    layout = QVBoxLayout()

    value_label = QLabel(value)
    value_label.setStyleSheet("font-size: 16pt; font-weight: bold; color: #2E86AB;")
    value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    layout.addWidget(value_label)
    widget.setLayout(layout)
    widget.setFixedSize(180, 80)

    return widget


def create_add_organization_dialog(parent):
    # Создает диалог добавления организации
    dialog = QDialog(parent)
    dialog.setWindowTitle("Добавить организацию")
    dialog.setModal(True)

    layout = QFormLayout()

    name_input = QLineEdit()
    inn_input = QLineEdit()
    address_input = QLineEdit()
    phone_input = QLineEdit()
    email_input = QLineEdit()

    layout.addRow("Название*:", name_input)
    layout.addRow("ИНН*:", inn_input)
    layout.addRow("Адрес:", address_input)
    layout.addRow("Телефон:", phone_input)
    layout.addRow("Email:", email_input)

    buttons = QDialogButtonBox(
        QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
    )

    def save_organization():
        QMessageBox.information(dialog, "Информация", "Организация будет сохранена здесь")
        dialog.accept()

    buttons.accepted.connect(save_organization)
    buttons.rejected.connect(dialog.reject)

    layout.addRow(buttons)
    dialog.setLayout(layout)

    return dialog


def create_add_product_dialog(parent):
    # Создает диалог добавления товара
    dialog = QDialog(parent)
    dialog.setWindowTitle("Добавить товар")
    dialog.setModal(True)

    layout = QFormLayout()

    org_combo = QComboBox()
    name_input = QLineEdit()
    category_input = QLineEdit()
    sku_input = QLineEdit()

    quantity_spin = QSpinBox()
    quantity_spin.setRange(0, 100000)
    quantity_spin.setValue(1)

    price_spin = QDoubleSpinBox()
    price_spin.setRange(0, 1000000)
    price_spin.setDecimals(2)
    price_spin.setValue(0)
    price_spin.setPrefix("₽ ")

    layout.addRow("Организация*:", org_combo)
    layout.addRow("Наименование*:", name_input)
    layout.addRow("Категория:", category_input)
    layout.addRow("Артикул:", sku_input)
    layout.addRow("Количество*:", quantity_spin)
    layout.addRow("Цена*:", price_spin)

    buttons = QDialogButtonBox(
        QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
    )

    def save_product():
        QMessageBox.information(dialog, "Информация", "Товар будет сохранен здесь")
        dialog.accept()

    buttons.accepted.connect(save_product)
    buttons.rejected.connect(dialog.reject)

    layout.addRow(buttons)
    dialog.setLayout(layout)

    return dialog


def create_transfer_dialog(parent):
    # Создает диалог перемещения товаров
    dialog = QDialog(parent)
    dialog.setWindowTitle("Перемещение товаров")
    dialog.setModal(True)
    dialog.resize(500, 400)

    layout = QVBoxLayout()

    form_layout = QFormLayout()

    from_org_combo = QComboBox()
    to_org_combo = QComboBox()
    product_combo = QComboBox()

    quantity_spin = QSpinBox()
    quantity_spin.setRange(1, 10000)

    form_layout.addRow("От организации*:", from_org_combo)
    form_layout.addRow("К организации*:", to_org_combo)
    form_layout.addRow("Товар*:", product_combo)
    form_layout.addRow("Количество*:", quantity_spin)

    layout.addLayout(form_layout)

    # Предпросмотр
    preview_group = QGroupBox("Предпросмотр операции")
    preview_layout = QVBoxLayout()
    preview_label = QLabel("Выберите организации и товар для просмотра деталей")
    preview_label.setWordWrap(True)
    preview_layout.addWidget(preview_label)
    preview_group.setLayout(preview_layout)
    layout.addWidget(preview_group)

    buttons = QDialogButtonBox(
        QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
    )

    def execute_transfer():
        QMessageBox.information(dialog, "Информация", "Перемещение товара будет выполнено здесь")
        dialog.accept()

    buttons.accepted.connect(execute_transfer)
    buttons.rejected.connect(dialog.reject)

    layout.addWidget(buttons)
    dialog.setLayout(layout)

    return dialog


def create_organization_details_dialog(parent):
    # Создает диалог деталей организации
    dialog = QDialog(parent)
    dialog.setWindowTitle("Детали организации: Тестовая организация")
    dialog.setModal(True)
    dialog.resize(600, 400)

    layout = QVBoxLayout()

    # Информация об организации
    info_group = QGroupBox("Информация об организации")
    info_layout = QFormLayout()

    info_layout.addRow("Название:", QLabel("Тестовая организация"))
    info_layout.addRow("ИНН:", QLabel("1234567890"))
    info_layout.addRow("Адрес:", QLabel("Адрес организации"))
    info_layout.addRow("Телефон:", QLabel("+7-XXX-XXX-XX-XX"))
    info_layout.addRow("Email:", QLabel("email@example.com"))
    info_layout.addRow("Дата создания:", QLabel("2024-01-01"))

    info_group.setLayout(info_layout)
    layout.addWidget(info_group)

    # Товары организации
    products_group = QGroupBox("Товары на складе")
    products_layout = QVBoxLayout()

    products_table = QTableWidget()
    products_table.setColumnCount(4)
    products_table.setHorizontalHeaderLabels([
        "Товар", "Категория", "Кол-во", "Цена"
    ])

    products_layout.addWidget(products_table)
    products_group.setLayout(products_layout)
    layout.addWidget(products_group)

    dialog.setLayout(layout)

    return dialog


def create_dashboard_tab():
    # Создает вкладку дашборда
    dashboard_tab = QWidget()
    layout = QVBoxLayout()

    # Заголовок
    title = QLabel("📊 Дашборд системы")
    title.setStyleSheet("font-size: 20pt; font-weight: bold; margin: 10px;")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(title)

    # Метрики
    metrics_layout = QHBoxLayout()

    metric_orgs = create_metric_widget("🏢 Организации", "0")
    metric_products = create_metric_widget("📦 Товары", "0")
    metric_value = create_metric_widget("💰 Стоимость", "0 руб")
    metric_transactions = create_metric_widget("🔄 Транзакции", "0")

    metrics_layout.addWidget(metric_orgs)
    metrics_layout.addWidget(metric_products)
    metrics_layout.addWidget(metric_value)
    metrics_layout.addWidget(metric_transactions)

    layout.addLayout(metrics_layout)

    # Статистика
    stats_layout = QHBoxLayout()

    # Левая панель - топ товаров
    left_panel = QGroupBox("🏆 Топ товаров по стоимости")
    left_layout = QVBoxLayout()
    top_products_list = QListWidget()
    left_layout.addWidget(top_products_list)
    left_panel.setLayout(left_layout)

    # Правая панель - последние операции
    right_panel = QGroupBox("📋 Последние операции")
    right_layout = QVBoxLayout()
    recent_transactions_list = QListWidget()
    right_layout.addWidget(recent_transactions_list)
    right_panel.setLayout(right_layout)

    stats_layout.addWidget(left_panel)
    stats_layout.addWidget(right_panel)

    layout.addLayout(stats_layout)

    dashboard_tab.setLayout(layout)
    return dashboard_tab


def create_organizations_tab(main_window):
    # Создает вкладку организаций
    org_tab = QWidget()
    layout = QVBoxLayout()

    # Панель управления
    control_layout = QHBoxLayout()

    add_org_btn = QPushButton("🏢 Добавить организацию")
    import_btn = QPushButton("📥 Импорт CSV")
    export_btn = QPushButton("📤 Экспорт в Excel")

    def add_organization():
        dialog = create_add_organization_dialog(main_window)
        dialog.exec()

    def import_csv():
        QMessageBox.information(main_window, "Информация", "Импорт CSV будет здесь")

    def export_excel():
        QMessageBox.information(main_window, "Информация", "Экспорт в Excel будет здесь")

    add_org_btn.clicked.connect(add_organization)
    import_btn.clicked.connect(import_csv)
    export_btn.clicked.connect(export_excel)

    control_layout.addWidget(add_org_btn)
    control_layout.addWidget(import_btn)
    control_layout.addWidget(export_btn)
    control_layout.addStretch()

    layout.addLayout(control_layout)

    # Таблица организаций
    orgs_table = QTableWidget()
    orgs_table.setColumnCount(6)
    orgs_table.setHorizontalHeaderLabels([
        "ID", "Название", "ИНН", "Адрес", "Телефон", "Товары"
    ])

    def show_organization_details(index):
        dialog = create_organization_details_dialog(main_window)
        dialog.exec()

    orgs_table.doubleClicked.connect(show_organization_details)
    layout.addWidget(orgs_table)

    org_tab.setLayout(layout)
    return org_tab


def create_products_tab(main_window):
    # Создает вкладку товаров
    products_tab = QWidget()
    layout = QVBoxLayout()

    # Фильтры и кнопки
    filter_layout = QHBoxLayout()

    org_filter = QComboBox()
    org_filter.addItem("Все организации")

    category_filter = QComboBox()
    category_filter.addItem("Все категории")

    search_input = QLineEdit()
    search_input.setPlaceholderText("🔍 Поиск товаров...")

    filter_layout.addWidget(QLabel("Организация:"))
    filter_layout.addWidget(org_filter)
    filter_layout.addWidget(QLabel("Категория:"))
    filter_layout.addWidget(category_filter)
    filter_layout.addWidget(search_input)
    filter_layout.addStretch()

    # Кнопка добавления товара
    add_product_btn = QPushButton("➕ Добавить товар")

    def add_product():
        dialog = create_add_product_dialog(main_window)
        dialog.exec()

    add_product_btn.clicked.connect(add_product)
    filter_layout.addWidget(add_product_btn)

    layout.addLayout(filter_layout)

    # Таблица товаров
    products_table = QTableWidget()
    products_table.setColumnCount(7)
    products_table.setHorizontalHeaderLabels([
        "ID", "Организация", "Наименование", "Категория", "Кол-во", "Цена", "Стоимость"
    ])

    layout.addWidget(products_table)

    products_tab.setLayout(layout)
    return products_tab


def create_transactions_tab(main_window):
    # Создает вкладку транзакций
    transactions_tab = QWidget()
    layout = QVBoxLayout()

    # Кнопки управления
    button_layout = QHBoxLayout()

    transfer_btn = QPushButton("🔄 Создать перемещение")
    generate_pdf_btn = QPushButton("📄 Создать отчет PDF")

    def create_transfer():
        dialog = create_transfer_dialog(main_window)
        dialog.exec()

    def generate_report():
        QMessageBox.information(main_window, "Информация", "Создание PDF отчета будет здесь")

    transfer_btn.clicked.connect(create_transfer)
    generate_pdf_btn.clicked.connect(generate_report)

    button_layout.addWidget(transfer_btn)
    button_layout.addWidget(generate_pdf_btn)
    button_layout.addStretch()

    layout.addLayout(button_layout)

    # Таблица транзакций
    transactions_table = QTableWidget()
    transactions_table.setColumnCount(8)
    transactions_table.setHorizontalHeaderLabels([
        "ID", "Дата", "От", "Кому", "Товар", "Кол-во", "Сумма", "Договор"
    ])

    def open_contract(index):
        QMessageBox.information(main_window, "Информация", "Открытие договора будет здесь")

    transactions_table.doubleClicked.connect(open_contract)
    layout.addWidget(transactions_table)

    transactions_tab.setLayout(layout)
    return transactions_tab


def main():
    # Главная функция приложения
    app = QApplication(sys.argv)

    # Устанавливаем стиль
    app.setStyle('Fusion')

    # Создаем главное окно
    main_window = QMainWindow()
    main_window.setWindowTitle("🏢 Organization Management System")
    main_window.setGeometry(100, 100, 1200, 800)

    # Центральный виджет с вкладками
    tab_widget = QTabWidget()
    main_window.setCentralWidget(tab_widget)

    # Создаем вкладки
    dashboard_tab = create_dashboard_tab()
    organizations_tab = create_organizations_tab(main_window)
    products_tab = create_products_tab(main_window)
    transactions_tab = create_transactions_tab(main_window)

    # Добавляем вкладки
    tab_widget.addTab(dashboard_tab, "📊 Дашборд")
    tab_widget.addTab(organizations_tab, "🏢 Организации")
    tab_widget.addTab(products_tab, "📦 Товары")
    tab_widget.addTab(transactions_tab, "📋 Транзакции")


    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()