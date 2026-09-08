# Автодеплой, бекап і rollback для Lokiravia

Для Lokiravia працює той самий пайплайн деплою, що й для Core: `.github/workflows/autodeploy.yml`
загортає виклик `scripts/autodeploy.py`.

## Ключові змінні GitHub Actions

1. `DEPLOY_DATA_PATHS` — директорії/файли для бекапу (рекомендовано шлях до `--data` каталогу).
2. `DEPLOY_PREPARE_COMMAND` — підготовка перед оновленням (необов’язково).
3. `DEPLOY_ACTIVATE_COMMAND` — команда rollout (обов’язково).
4. `DEPLOY_ROLLBACK_COMMAND` — rollback команди.
5. `DEPLOY_HEALTH_COMMAND` — перевірка працездатності.
6. `DEPLOY_RELEASE_NOTES_COMMAND` — команда отримання release notes.

## Що бекапимо в Lokiravia

`lokiravia` зберігає клієнтські дані у директорії з `--data` аргументом:

- `briefs.sqlite3`
- `core-intake.sqlite3`

Тому `DEPLOY_DATA_PATHS` зазвичай має вказувати саме цю директорію (наприклад `data`), або окремо обидва файли.

## Рекомендуваний мінімальний сет команд

```sh
DEPLOY_PREPARE_COMMAND="git fetch origin main && git reset --hard origin/main"
DEPLOY_ACTIVATE_COMMAND="supervisorctl restart lokiravia"
DEPLOY_ROLLBACK_COMMAND="supervisorctl restart lokiravia"
DEPLOY_HEALTH_COMMAND="curl -fsS http://127.0.0.1:8767/healthz"
DEPLOY_RELEASE_NOTES_COMMAND="git log -1 --pretty=%B"
```

Актуальний процесор порту/хоста підставте під вашу production інфраструктуру.

## Вимога безперервності

- Уникайте довгих downtime: активація має виконуватися через безперервне перенаправлення (blue-green або swap link).
- Резервні копії і rollback працюють перед змінами даних і мають бути останньою лінією захисту.
- `DEPLOY_ROLLBACK_COMMAND` повинен повертати попередній стабільний стан сервісу, якщо `DEPLOY_ACTIVATE_COMMAND` або health check не пройшли.

## Де дивитися статус

Сторінка у спільному дашборді: `docs/deploy-dashboard.html` у репозиторії Lokvetia Core.
