import sys
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    
    parts = line.strip().split(" ", 3)
    if len(parts) == 4:
        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3]
        }
    return {}

def load_logs(file_path: str) -> List[dict]:
    
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Пропускаємо порожні рядки
                if not line.strip():
                    continue
                
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
                    
    except FileNotFoundError:
        print(f"Помилка: Файл логів за шляхом '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Сталася непередбачена помилка при читанні файлу: {e}")
        sys.exit(1)
        
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
   
    filtered = filter(lambda log: log['level'].upper() == level.upper(), logs)
    return list(filtered)

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py /path/to/logfile.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    
    logs = load_logs(file_path)
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) >= 3:
        level_filter = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level_filter)
        
        print(f"\nДеталі логів для рівня '{level_filter}':")
        if not filtered_logs:
            print("Записів такого рівня не знайдено.")
        else:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()